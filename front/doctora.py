import tkinter as tk
from tkinter import messagebox,Canvas
from tkinter import ttk
from frontend_utils import load_image  # Reutilizar la lógica de carga de imágenes
import requests
from PIL import Image, ImageTk

class DoctoraPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Página de la Dra. Sonrisa")
        self.root.state('zoomed')
        self.root.config(bg="white")

        # ==================== Cargar la imagen de fondo =======================
        self.cargar_fondo()

        # ==================== Header con nombre de la Dra. Sonrisa =======================
        self.header = tk.Frame(self.root, bg='#98a65d', height=80)
        self.header.pack(fill='x')

        self.title = tk.Label(self.header, text="Bienvenida, Dra. Sonrisa", 
                              font=("Arial", 24, "bold"), bg="#98a65d", fg="white")
        self.title.place(x=20, y=20)

        # ==================== Menú Lateral =======================
        self.side_menu = tk.Frame(self.root, bg="pink", width=280)
        self.side_menu.pack(side='left', fill='y')

        # Botón para ver todas las citas
        self.btn_ver_todas_citas = tk.Button(self.side_menu, text="Ver Todas las Citas", font=("Arial", 16), 
                                              bg="pink", fg="black", bd=0, cursor="hand2", 
                                              command=self.mostrar_todas_citas)
        self.btn_ver_todas_citas.place(x=20, y=100, width=200, height=40)

        # Botón para administrar profesionales
        self.btn_admin_profesionales = tk.Button(self.side_menu, text="Administrar Profesionales", font=("Arial", 16), 
                                                  bg="pink", fg="black", bd=0, cursor="hand2", 
                                                  command=self.administrar_profesionales)
        self.btn_admin_profesionales.place(x=20, y=160, width=250, height=40)

        # Botón para informes financieros
        self.btn_informes_financieros = tk.Button(self.side_menu, text="Informes Financieros", font=("Arial", 16), 
                                                   bg="pink", fg="black", bd=0, cursor="hand2", 
                                                   command=self.mostrar_informes_financieros)
        self.btn_informes_financieros.place(x=20, y=220, width=200, height=40)

        # ==================== Área principal =======================
        self.content = tk.Frame(self.root, bg="white")
        self.content.pack(side="left", fill="both", expand=False)
    """def cargar_fondo(self):
        # Crear un canvas para la imagen de fondo
        self.canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        bg_frame = load_image('fondo1.jpg')  # Asegúrate de que esta función esté correctamente definida

        if bg_frame:
            # Ajustar el tamaño de la imagen al tamaño de la ventana
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            bg_frame = bg_frame.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

            # Guardar la imagen como un atributo de la clase para que no sea recolectada
            self.photo = ImageTk.PhotoImage(bg_frame)

            # Colocar la imagen en el canvas
            self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

            # Aplicar un degradado semitransparente (con un color sólido y transparencia)
            self.canvas.create_rectangle(0, 0, screen_width, screen_height, fill="white", stipple="gray50")"""

    def cargar_fondo(self):
        # Crear un canvas para la imagen de fondo
        self.canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        bg_frame = load_image('fondo1.jpg')  # Asegúrate de que esta función esté correctamente definida

        if bg_frame:
            # Ajustar el tamaño de la imagen al tamaño de la ventana
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            bg_frame = bg_frame.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

            # Guardar la imagen como un atributo de la clase para que no sea recolectada
            self.photo = ImageTk.PhotoImage(bg_frame)

            # Colocar la imagen en el canvas
            self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

            # Aplicar un degradado semitransparente (con un color sólido y transparencia)
            self.canvas.create_rectangle(0, 0, screen_width, screen_height, fill="white")

        # Asegurar que el canvas esté detrás de los otros widgets
        #self.canvas.lower()  # Coloca el canvas detrás de los demás widgets



    def mostrar_todas_citas(self):
        # Limpiar el área principal y mostrar todas las citas
        for widget in self.content.winfo_children():
            widget.destroy()

        citas_label = tk.Label(self.content, text="Todas las Citas", font=("Arial", 20), bg="white")
        citas_label.pack(pady=20)
        # Llamada a la API para obtener citas
        self.mostrar_datos_citas_api("http://127.0.0.1:8000/reservas/total")

    def administrar_profesionales(self):
        # Limpiar el área principal
        for widget in self.content.winfo_children():
            widget.destroy()

        # Título de la sección
        profesionales_label = tk.Label(self.content, text="Administrar Profesionales", font=("Arial", 20), bg="#AAFF00")
        profesionales_label.pack(pady=20)

        # Título de la sección de búsqueda por rango de fecha
        rango_fecha_label = tk.Label(self.content, text="Buscar Profesionales por Rango de Fecha", font=("Arial", 20), bg="#AAFF00")
        rango_fecha_label.pack(pady=20)

        # Campo de entrada para ingresar el ID del profesional
        self.professional_id_label = tk.Label(self.content, text="Ingresar ID del Profesional:", font=("Arial", 14))
        self.professional_id_label.pack(pady=5)
        self.professional_id_entry = tk.Entry(self.content, font=("Arial", 14))
        self.professional_id_entry.pack(pady=5)

        # Campo de fecha de inicio
        self.fecha_inicio_label = tk.Label(self.content, text="Fecha de Inicio (aaaa-mm-dd):", font=("Arial", 14))
        self.fecha_inicio_label.pack(pady=5)
        self.fecha_inicio_entry = tk.Entry(self.content, font=("Arial", 14))
        self.fecha_inicio_entry.pack(pady=5)

        # Campo de fecha de fin
        self.fecha_fin_label = tk.Label(self.content, text="Fecha de Fin (aaaa-mm-dd):", font=("Arial", 14))
        self.fecha_fin_label.pack(pady=5)
        self.fecha_fin_entry = tk.Entry(self.content, font=("Arial", 14))
        self.fecha_fin_entry.pack(pady=5)

        # Botón para buscar profesionales
        self.btn_buscar = tk.Button(self.content, text="Buscar", font=("Arial", 14), command=self.mostrar_profesionales_por_fecha)
        self.btn_buscar.pack(pady=20)

    def mostrar_profesionales_por_fecha(self):
        # Obtener la selección del profesional
        trabajador_id = self.professional_id_entry.get()

        # Obtener las fechas ingresadas
        fecha_inicio = self.fecha_inicio_entry.get()
        fecha_fin = self.fecha_fin_entry.get()

        # Validar las fechas
        if not fecha_inicio or not fecha_fin or not trabajador_id:
            messagebox.showerror("Error", "Por favor ingrese ambas fechas y seleccione un profesional.")
            return

        # Llamada a la API o base de datos para obtener los servicios por fechas
        url = f"http://127.0.0.1:8000//reservas/profesional/{fecha_inicio}/{fecha_fin}/{trabajador_id}"
        self.mostrar_datos_api(url)

        # Limpiar el área de contenido para mostrar los resultados
        for widget in self.content.winfo_children():
            widget.destroy()

        # Título de los resultados
        resultados_label = tk.Label(self.content, text=f"Resultados para el profesional(ID: {trabajador_id}) entre {fecha_inicio} y {fecha_fin}", font=("Arial", 20), bg="#AAFF00")
        resultados_label.pack(pady=20)

    def mostrar_datos_api(self, url, encabezados, campos):
    #"""Método general para obtener datos de la API y mostrarlos en formato de tabla."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                datos = response.json()
                if len(datos) == 0:
                    messagebox.showinfo("Sin resultados", "No se encontraron resultados para la solicitud.")
                    return

                # Limpiar el área de contenido para mostrar los resultados
                for widget in self.content.winfo_children():
                    widget.destroy()

                # Crear un Frame semitransparente para los resultados
                resultados_frame = tk.Frame(self.content, bg="white", bd=2)
                resultados_frame.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")

                # Hacer que las columnas se expandan y llenen el espacio disponible
                self.content.grid_rowconfigure(0, weight=1)
                for col_idx in range(len(encabezados)):
                    self.content.grid_columnconfigure(col_idx, weight=1)

                # Título de los resultados
                resultados_label = tk.Label(resultados_frame, text="Resultados", font=("Arial", 20), bg="#00CC66", fg="white")
                resultados_label.grid(row=0, column=0, columnspan=len(encabezados), pady=10, sticky="ew")

                # Mostrar encabezados
                for idx, encabezado in enumerate(encabezados):
                    tk.Label(resultados_frame, text=encabezado, font=("Arial", 14, "bold"), 
                            bg="#00CC66", fg="white", width=20, relief="solid", anchor="w", padx=5).grid(row=1, column=idx, padx=5, pady=5, sticky="ew")

                # Mostrar los resultados
                for row_idx, fila in enumerate(datos, start=2):
                    for col_idx, campo in enumerate(campos):
                        tk.Label(resultados_frame, text=fila.get(campo, "Desconocido"), font=("Arial", 12), bg="white", width=20, 
                                anchor="w", relief="solid", padx=5).grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="ew")
            else:
                messagebox.showerror("Error", f"Error al obtener datos de la API: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al conectar con la API: {e}")


    def mostrar_todas_citas(self):
    # Limpiar el área principal y mostrar todas las citas
        for widget in self.content.winfo_children():
            widget.destroy()

        # Llamada a la API para obtener citas
        url = "http://127.0.0.1:8000/reservas/total"
        encabezados = ["Cliente", "Servicio", "Trabajador", "Fecha"]
        campos = ["Cliente", "Servicio", "Trabajador", "fecha"]
        self.mostrar_datos_api(url, encabezados, campos)
    def mostrar_profesionales_por_fecha(self):
        # Obtener la selección del profesional
        trabajador_id = self.professional_id_entry.get()

        # Obtener las fechas ingresadas
        fecha_inicio = self.fecha_inicio_entry.get()
        fecha_fin = self.fecha_fin_entry.get()

        # Validar las fechas
        if not fecha_inicio or not fecha_fin or not trabajador_id:
            messagebox.showerror("Error", "Por favor ingrese ambas fechas y seleccione un profesional.")
            return

        # Encabezados y campos que queremos mostrar
        encabezados = ["Cliente", "Servicio", "Trabajador", "Fecha"]
        campos = ["Cliente", "Servicio", "Trabajador", "fecha"]

        # Llamada a la API para obtener los servicios por fechas
        url = f"http://127.0.0.1:8000/reservas/profesional/{fecha_inicio}/{fecha_fin}/{trabajador_id}"
        self.mostrar_datos_api(url, encabezados, campos)

    def mostrar_informes_financieros(self):
        # Limpiar el área principal antes de mostrar los informes financieros
        for widget in self.content.winfo_children():
            widget.destroy()

        informes_label = tk.Label(self.content, text="Informes Financieros", font=("Arial", 20), bg="white")
        informes_label.pack(pady=20)

        # Encabezados y campos que queremos mostrar
        encabezados = ["ID Pago", "Cliente ID", "Monto", "Método de Pago", "Fecha", "Reserva ID"]
        campos = ["id", "cliente_id", "monto", "metodo_pago", "fecha", "reserva_id"]

        # Llamada a la API para obtener los informes financieros (pagos)
        url = "http://127.0.0.1:8000/Pagos/"
        self.mostrar_datos_api(url, encabezados, campos)
# Para mostrar la página de la Dra. Sonrisa después de loguearse correctamente

def mostrar_pagina_doctora():
    root = tk.Tk()
    app = DoctoraPage(root)
    root.mainloop()

