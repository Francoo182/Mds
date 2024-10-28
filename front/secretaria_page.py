import tkinter as tk
from tkinter import Canvas, messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import requests
from frontend_utils import load_image

class SecretariaPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Página de la Secretaria")
        self.root.state('zoomed')

        # ==================== Cargar la imagen de fondo =======================

        self.cargar_fondo()

        # ==================== Header con nombre de la secretaria =======================
        self.header = tk.Frame(self.root, bg='#98a65d', height=80)
        self.header.pack(fill='x')

        self.title = tk.Label(self.header, text="Bienvenida, Secretaria", 
                              font=("Arial", 24, "bold"), bg="#98a65d", fg="white")
        self.title.place(x=80, y=20)

        # ==================== Menú Lateral =======================
        self.side_menu = tk.Frame(self.root, bg="pink", width=380)
        self.side_menu.pack(side='left', fill='y')

        # Botón para ocultar/mostrar el menú lateral
        self.btn_toggle_menu = tk.Button(self.header, text="☰", font=("Arial", 16),
                                          command=self.toggle_menu, bg="#98a65d", fg="white")
        self.btn_toggle_menu.place(x=20, y=20)

        # Botón para "Crear Empleado"
        self.btn_crear_empleado = tk.Button(self.side_menu, text="Crear Empleado", font=("Arial", 16), 
                                            bg="pink", fg="black", bd=0, cursor="hand2", 
                                            command=self.crear_empleado)
        self.btn_crear_empleado.place(x=10, y=60, width=150, height=40)

        # Botón para "Listado de Clientes"
        self.btn_listado_clientes = tk.Button(self.side_menu, text="Listado de Clientes", font=("Arial", 16), 
                                              bg="pink", fg="black", bd=0, cursor="hand2", 
                                              command=self.listado_clientes)
        self.btn_listado_clientes.place(x=10, y=120, width=180, height=40)

        # Botón para "Listado de Clientes a Atender por Día"
        self.btn_listado_clientes_dia = tk.Button(self.side_menu, text="Listado de Clientes a Atender por Día", font=("Arial", 16), 
                                                  bg="pink", fg="black", bd=0, cursor="hand2", 
                                                  command=self.listado_clientes_dia)
        self.btn_listado_clientes_dia.place(x=10, y=180, width=350, height=40)

        # Botón para "Ingresos en un Rango de Fecha (DESCARGAR)"
        self.btn_ingresos_rango_fecha = tk.Button(self.side_menu, text="Ingresos en un Rango de Fecha", font=("Arial", 16), 
                                                  bg="pink", fg="black", bd=0, cursor="hand2", 
                                                  command=self.ingresos_rango_fecha)
        self.btn_ingresos_rango_fecha.place(x=10, y=240, width=300, height=40)

        # Botón para "Listado de Clientes por Profesional"
        self.btn_listado_clientes_profesional = tk.Button(self.side_menu, text="Listado de Clientes por Profesional", font=("Arial", 16), 
                                                          bg="pink", fg="black", bd=0, cursor="hand2", 
                                                          command=self.administrar_profesionales)
        self.btn_listado_clientes_profesional.place(x=10, y=300, width=330, height=40)

        # Botón para "Atras"
        self.btn_listado_clientes_profesional = tk.Button(self.side_menu, text="Atras", font=("Arial", 16), 
                                                          bg="pink", fg="black", bd=0, cursor="hand2", 
                                                          command=self.atras)
        self.btn_listado_clientes_profesional.place(x=10, y=360, width=50, height=40)

        # ==================== Área principal =======================
        self.content = tk.Frame(self.root)
        self.content.pack(side="left", fill="both", expand=False)

    def cargar_fondo(self):
        # Crear un canvas para la imagen de fondo
        self.canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        bg_frame = load_image('fondo1.jpg')   # Asegúrate de que esta función esté correctamente definida

        if bg_frame:
            # Ajustar el tamaño de la imagen al tamaño de la ventana
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            bg_frame = bg_frame.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

            # Guardar la imagen como un atributo de la clase para que no sea recolectada
            self.photo = ImageTk.PhotoImage(bg_frame)

            # Colocar la imagen en el canvas
            self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
            print("Imagen cargada y colocada en el canvas.")  # Mensaje de depuración

            # Crear un rectángulo con color semitransparente
            self.canvas.create_rectangle(0, 0, screen_width, screen_height, fill="#000000", stipple='gray25')
        else:
            print("No se pudo cargar la imagen de fondo.")  # Mensaje de depuración

        # Forzar la actualización de la ventana
        self.root.update_idletasks()

    def toggle_menu(self):
        if self.side_menu.winfo_viewable():
            self.side_menu.pack_forget()  # Ocultar el menú lateral
        else:
            self.side_menu.pack(side="left", fill="y")  # Mostrar en el lado izquierdo
        for widget in self.content.winfo_children():
            widget.destroy()
        self.content.destroy()
        self.content = tk.Frame(self.root)
        self.content.pack(side="left", fill="both", expand=False)
        
    def mostrar_datos_api(self, url, encabezados, campos):
            # Método general para obtener datos de la API y mostrarlos en formato de tabla.
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
                    resultados_frame.grid(row=0, column=0, pady=10, padx=10, sticky="n")

                    # Configuración para que las columnas se expandan horizontalmente, pero no las filas
                    self.content.grid_columnconfigure(0, weight=1)
                    resultados_frame.grid_columnconfigure(0, weight=1)
                    for col_idx in range(len(encabezados)):
                        resultados_frame.grid_columnconfigure(col_idx, weight=1)

                    # Título de los resultados
                    resultados_label = tk.Label(resultados_frame, text="Resultados", font=("Arial", 10), bg="#00CC66", fg="white")
                    resultados_label.grid(row=0, column=0, columnspan=len(encabezados), pady=10, sticky="ew")

                    # Mostrar encabezados
                    for idx, encabezado in enumerate(encabezados):
                        tk.Label(resultados_frame, text=encabezado, font=("Arial", 14, "bold"), 
                                bg="#00CC66", fg="white", width=20, relief="solid", anchor="w", padx=5).grid(row=1, column=idx, padx=5, pady=5, sticky="ew")

                    # Mostrar los resultados
                    for row_idx, fila in enumerate(datos, start=2):
                        for col_idx, campo in enumerate(campos):
                            tk.Label(resultados_frame, text=fila.get(campo, "Desconocido"), font=("Arial", 12), bg="white", width=10, 
                                    anchor="w", relief="solid", padx=5).grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="ew")
                else:
                    messagebox.showerror("Error", f"Error al obtener datos de la API: {response.status_code}")
            except Exception as e:
                messagebox.showerror("Error", f"Hubo un problema al conectar con la API: {e}")

    def crear_empleado(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        # Título de la sección
        empleado_label = tk.Label(self.content, text="Crear Empleado", font=("Arial", 20))
        empleado_label.pack(pady=20)

        # Campo de texto para Nombre
        nombre_label = tk.Label(self.content, text="Nombre")
        nombre_label.pack(pady=(10, 0))
        nombre_entry = tk.Entry(self.content)
        nombre_entry.pack()

        # Campo de texto para Email
        email_label = tk.Label(self.content, text="Email")
        email_label.pack(pady=(10, 0))
        email_entry = tk.Entry(self.content)
        email_entry.pack()

        # Campo de texto para Contraseña
        password_label = tk.Label(self.content, text="Contraseña")
        password_label.pack(pady=(10, 0))
        password_entry = tk.Entry(self.content, show="*")
        password_entry.pack()

        # Campo de texto para Rol
        rol_label = tk.Label(self.content, text="Rol")
        rol_label.pack(pady=(10, 0))
        rol_var = tk.StringVar()
        rol_combobox = ttk.Combobox(self.content, textvariable=rol_var)
        rol_combobox['values'] = ("Doctora", "Profesional", "Secretaria")
        rol_combobox.pack()

        url = "http://127.0.0.1:8000/workers/"

        # Botón para enviar los datos
        submit_button = tk.Button(
            self.content, 
            text="Registrar Empleado", 
            command=lambda: self.cargar_datos_api(
                url, 
                nombre_entry.get(),  # Ahora obtiene el valor al hacer clic
                email_entry.get(), 
                password_entry.get(), 
                rol_var.get()
            )
        )
        submit_button.pack(pady=20)

    def listado_clientes(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        clientes_label = tk.Label(self.content, text="Listado de Clientes", font=("Arial", 20))
        clientes_label.pack(pady=1)

        encabezados = ["ID Cliente", "Nombre", "email", "Telefono"]
        campos = ["id", "nombre", "email", "telefono"]

        url ="http://127.0.0.1:8000/clientsg/"
        self.mostrar_datos_api(url, encabezados, campos)

    def listado_clientes_dia(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        clientes_dia_label = tk.Label(self.content, text="Listado de Clientes a Atender por Día", font=("Arial", 20))
        clientes_dia_label.pack(pady=1)

        # Campo de fecha de inicio
        self.fecha_label = tk.Label(self.content, text="Fecha de Inicio (aaaa-mm-dd):", font=("Arial", 14))
        self.fecha_label.pack(pady=5)
        self.fecha_entry = tk.Entry(self.content, font=("Arial", 14))
        self.fecha_entry.pack(pady=5)

        # Botón para buscar con la fecha ingresada
        btn_buscar = tk.Button(self.content, text="Buscar", font=("Arial", 14), command=self.buscar_clientes_dia)
        btn_buscar.pack(pady=10)

    def buscar_clientes_dia(self):
        # Construir el URL dinámicamente después de obtener la fecha
        fecha = self.fecha_entry.get()
        if not fecha:
            messagebox.showerror("Error", "Por favor ingrese una fecha.")
            return
        url = f"http://127.0.0.1:8000/reservasf/{fecha}"
        encabezados = ["Cliente", "Servicio", "Trabajador", "Fecha"]
        campos = ["cliente", "servicio", "trabajador", "fecha"]
        self.mostrar_datos_api(url, encabezados, campos)

    def ingresos_rango_fecha(self):
    # Limpia el contenido actual
        for widget in self.content.winfo_children():
            widget.destroy()

        # Título
        ingresos_label = tk.Label(self.content, text="Ingresos en un Rango de Fecha", font=("Arial", 20))
        ingresos_label.pack(pady=1)
        
        # Campo de entrada para fecha de inicio
        self.fecha_inicio_label = tk.Label(self.content, text="Ingresar Fecha inicio:", font=("Arial", 14))
        self.fecha_inicio_label.pack(pady=5)
        self.fecha_inicio_entry = tk.Entry(self.content, font=("Arial", 14))
        self.fecha_inicio_entry.pack(pady=5)
        
        # Campo de entrada para fecha de fin
        self.fecha_fin_label = tk.Label(self.content, text="Ingresar Fecha fin:", font=("Arial", 14))
        self.fecha_fin_label.pack(pady=5)
        self.fecha_fin_entry = tk.Entry(self.content, font=("Arial", 14))
        self.fecha_fin_entry.pack(pady=5)
        # Botón para buscar datos y llamar a la función con las fechas ingresadas
        descargar_button = tk.Button(
            self.content, 
            text="DESCARGAR", 
            command=lambda: self.mostrar_datos_api2(
                f"http://127.0.0.1:8000/informe/ingresos/{self.fecha_inicio_entry.get()}/{self.fecha_fin_entry.get()}",
            )
        )
        descargar_button.pack(pady=10)
        
        # Encabezados y campos de la tabla
    def mostrar_datos_api2(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                messagebox.showinfo("Completado","PDF descargado en el rango de fecha seleccionado")
            else: messagebox.showerror("Error", f"Error al obtener datos de la API: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al conectar con la API: {e}")

    def administrar_profesionales(self):
        # Limpiar el área principal
        for widget in self.content.winfo_children():
            widget.destroy()

        # Título de la sección
        profesionales_label = tk.Label(self.content, text="Administrar Profesionales", font=("Arial", 20))
        profesionales_label.pack(pady=20)

        # Título de la sección de búsqueda por rango de fecha
        rango_fecha_label = tk.Label(self.content, text="Buscar Profesionales por Rango de Fecha", font=("Arial", 20))
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
        # Encabezados y campos que queremos mostrar
        encabezados = ["Cliente", "Servicio", "Trabajador", "Fecha"]
        campos = ["cliente", "Servicio", "Trabajador", "fecha"]

        # Llamada a la API para obtener los servicios por fechas
        url = f"http://127.0.0.1:8000/reservas/profesional/{fecha_inicio}/{fecha_fin}/{trabajador_id}"
        self.mostrar_datos_api(url, encabezados, campos)

    def atras(self):
        for widget in self.content.winfo_children():
            widget.destroy()
        self.content.destroy()
        self.content = tk.Frame(self.root)
        self.content.pack(side="left", fill="both", expand=False)

# Para ejecutar la ventana de secretaria
def mostrar_pagina_secretaria():
    root = tk.Tk()
    SecretariaPage(root)
    root.mainloop()
