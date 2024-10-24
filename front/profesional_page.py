import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class ProfesionalPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Página del Profesional")
        self.root.geometry("1266x712")
        self.root.state('zoomed')
        self.root.config(bg="white")

        # ==================== Header con nombre del profesional =======================
        self.header = tk.Frame(self.root, bg='#98a65d', height=80)
        self.header.pack(fill='x')

        self.title = tk.Label(self.header, text="Bienvenido, Profesional", 
                              font=("Arial", 24, "bold"), bg="#98a65d", fg="white")
        self.title.place(x=20, y=20)

        # ==================== Menú Lateral =======================
        self.side_menu = tk.Frame(self.root, bg="pink", width=250)
        self.side_menu.pack(side='left', fill='y')

        # Botón para ver citas
        self.btn_ver_citas = tk.Button(self.side_menu, text="Ver Citas", font=("Arial", 16), 
                                        bg="pink", fg="black", bd=0, cursor="hand2", 
                                        command=self.mostrar_citas)
        self.btn_ver_citas.place(x=20, y=100, width=200, height=40)

        # Botón para servicios realizados
        self.btn_servicios_realizados = tk.Button(self.side_menu, text="Servicios Realizados", font=("Arial", 16), 
                                                   bg="pink", fg="black", bd=0, cursor="hand2", 
                                                   command=self.mostrar_servicios_realizados)
        self.btn_servicios_realizados.place(x=20, y=160, width=200, height=40)

        # Botón para reportes
        self.btn_reportes = tk.Button(self.side_menu, text="Generar Reportes", font=("Arial", 16), 
                                       bg="pink", fg="black", bd=0, cursor="hand2", 
                                       command=self.generar_reportes)
        self.btn_reportes.place(x=20, y=220, width=200, height=40)

        # ==================== Área principal =======================
        self.content = tk.Frame(self.root, bg="white")
        self.content.pack(side="left", fill="both", expand=True)

    def mostrar_citas(self):
        # Limpiar el área principal y mostrar citas agendadas
        for widget in self.content.winfo_children():
            widget.destroy()

        # Cargar y colocar el fondo
        citas_frame = Image.open('images\\bg3.jpg')
        photo = ImageTk.PhotoImage(citas_frame)
        citas_frame_panel = tk.Label(self.content, image=photo)
        citas_frame_panel.image = photo
        citas_frame_panel.place(x=0, y=0, relwidth=1, relheight=1)

        # Colocar el texto encima del fondo
        citas_label = tk.Label(self.content, text="Citas Agendadas", font=("Arial", 20), bg="white")
        citas_label.pack(pady=20)

    def mostrar_servicios_realizados(self):
        # Limpiar el área principal y mostrar los servicios realizados
        for widget in self.content.winfo_children():
            widget.destroy()

        # Cargar y colocar el fondo
        servicios_frame = Image.open('images\\bg3.jpg')
        photo = ImageTk.PhotoImage(servicios_frame)
        servicios_frame_panel = tk.Label(self.content, image=photo)
        servicios_frame_panel.image = photo
        servicios_frame_panel.place(x=0, y=0, relwidth=1, relheight=1)

        # Colocar el texto encima del fondo
        servicios_label = tk.Label(self.content, text="Servicios Realizados", font=("Arial", 20), bg="white")
        servicios_label.pack(pady=20)

    def generar_reportes(self):
        # Limpiar el área principal y mostrar opciones para generar reportes
        for widget in self.content.winfo_children():
            widget.destroy()

        # Cargar y colocar el fondo
        reportes_frame = Image.open('images\\bg3.jpg')
        photo = ImageTk.PhotoImage(reportes_frame)
        reportes_frame_panel = tk.Label(self.content, image=photo)
        reportes_frame_panel.image = photo
        reportes_frame_panel.place(x=0, y=0, relwidth=1, relheight=1)

        # Colocar el texto encima del fondo
        reportes_label = tk.Label(self.content, text="Generar Reportes", font=("Arial", 20), bg="white")
        reportes_label.pack(pady=20)
        # Aquí puedes agregar widgets para seleccionar los tipos de reportes a generar

# Para ejecutar la ventana de profesional
def mostrar_pagina_profesional():
    root = tk.Tk()
    app = ProfesionalPage(root)
    root.mainloop()
