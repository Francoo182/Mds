import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import uvicorn

# Función para generar factura en PDF usando ReportLab
def generar_factura_pdf(cliente, pago, reserva, servicio):
    nombre_archivo = f"factura_{cliente['nombre']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2.0, height - 40, "Factura de pago - Spa")

    # Información del cliente
    c.setFont("Helvetica", 12)
    y = height - 80
    c.drawString(50, y, f"Cliente: {cliente['nombre']}")
    y -= 20
    c.drawString(50, y, f"Email: {cliente['email']}")
    y -= 20
    c.drawString(50, y, f"Teléfono: {cliente['telefono']}")
    
    # Detalles del servicio y pago
    y -= 40
    c.drawString(50, y, f"Servicio: {servicio['nombre']}")
    y -= 20
    c.drawString(50, y, f"Descripción: {servicio['descripcion']}")
    y -= 20
    c.drawString(50, y, f"Fecha de reserva: {reserva['fecha'].strftime('%Y-%m-%d %H:%M')}")
    y -= 20
    c.drawString(50, y, f"Monto: ${pago['monto']}")
    y -= 20
    c.drawString(50, y, f"Método de pago: {pago['metodo_pago']}")
    y -= 20
    c.drawString(50, y, f"Fecha de pago: {pago['fecha'].strftime('%Y-%m-%d %H:%M')}")

    # Guardar el archivo PDF
    c.save()

    return nombre_archivo

# Función para enviar factura por email
def enviar_factura_por_email(cliente_email, archivo_factura):
    from_email = "tu_correo@example.com"
    from_password = "tu_contraseña"
    to_email = cliente_email

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Factura de Pago - Spa'

    # Cuerpo del mensaje
    body = "Adjuntamos la factura de tu reserva en el spa. ¡Gracias por tu visita!"
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo PDF
    with open(archivo_factura, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={archivo_factura}")
        msg.attach(part)

    # Enviar el correo
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Correo enviado con éxito")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
