"""importaciones"""



from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from fastapi import APIRouter
import crud
from models import Cliente, Pago, Reserva, Servicio

router = APIRouter()

def generar_factura(cliente: Cliente, pago: Pago, reserva: Reserva, servicio: Servicio):
    nombre_archivo = f"factura_{cliente.nombre}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2.0, height - 40, "Factura de pago - Spa")

    # Información del cliente
    c.setFont("Helvetica", 12)
    y = height - 80
    c.drawString(50, y, f"Cliente: {cliente.nombre}")
    y -= 20
    c.drawString(50, y, f"Email: {cliente.email}")
    y -= 20
    c.drawString(50, y, f"Teléfono: {cliente.telefono}")

    # Detalles del servicio y pago
    y -= 40
    c.drawString(50, y, f"Servicio: {servicio.nombre}")
    y -= 20
    c.drawString(50, y, f"Descripción: {servicio.descripcion}")
    y -= 20
    c.drawString(50, y, f"Fecha de reserva: {reserva.fecha.strftime('%Y-%m-%d %H:%M')}")
    y -= 20
    c.drawString(50, y, f"Monto: ${pago.monto}")
    y -= 20
    c.drawString(50, y, f"Método de pago: {pago.metodo_pago}")
    y -= 20
    c.drawString(50, y, f"Fecha de pago: {pago.fecha.strftime('%Y-%m-%d %H:%M')}")

    # Guardar el PDF
    c.save()

    return nombre_archivo


@router.get("/Pagos/")
def get_pagos():
    return crud.get_Payments_xday()
