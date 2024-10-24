import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class SecretariaPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Página de Secretaria")
        self.root.geometry("1266x712")
        self.root.state('zoomed')
        self.root.config(bg="white")

        # ==================== Header con nombre de la secretaria =======================
        self.header = tk.Frame(self.root, bg='#98a65d', height=80)
        self.header.pack(fill='x')

        self.title = tk.Label(self.header, text="Bienvenida, Secretaria", 
                              font=("Arial", 24, "bold"), bg="#98a65d", fg="white")
        self.title.place(x=20, y=20)

        # ==================== Menú Lateral =======================
        self.side_menu = tk.Frame(self.root, bg="pink", width=250)
        self.side_menu.pack(side='left', fill='y')

        # Botón para listado de pagos
        self.btn_listado_pagos = tk.Button(self.side_menu, text="Listado de Pagos", font=("Arial", 16), 
                                            bg="pink", fg="black", bd=0, cursor="hand2", 
                                            command=self.mostrar_listado_pagos)
        self.btn_listado_pagos.place(x=20, y=100, width=200, height=40)

        # Botón para registrar pago
        self.btn_registrar_pago = tk.Button(self.side_menu, text="Registrar Pago", font=("Arial", 16), 
                                             bg="pink", fg="black", bd=0, cursor="hand2", 
                                             command=self.mostrar_registrar_pago)
        self.btn_registrar_pago.place(x=20, y=160, width=200, height=40)

        # Botón para generar informes
        self.btn_generar_informes = tk.Button(self.side_menu, text="Generar Informes", font=("Arial", 16), 
                                               bg="pink", fg="black", bd=0, cursor="hand2", 
                                               command=self.mostrar_generar_informes)
        self.btn_generar_informes.place(x=20, y=220, width=200, height=40)

        # ==================== Área principal =======================
        self.content = tk.Frame(self.root, bg="white")
        self.content.pack(side="left", fill="both", expand=True)

    def mostrar_listado_pagos(self):
        # Limpiar el área principal y mostrar el listado de pagos
        for widget in self.content.winfo_children():
            widget.destroy()

        # Cargar y colocar el fondo
        pagos_frame = Image.open('images\\bg3.jpg')
        photo = ImageTk.PhotoImage(pagos_frame)
        pagos_frame_panel = tk.Label(self.content, image=photo)
        pagos_frame_panel.image = photo
        pagos_frame_panel.place(x=0, y=0, relwidth=1, relheight=1)

        # Colocar el texto encima del fondo
        listado_label = tk.Label(self.content, text="Listado de Pagos", font=("Arial", 20), bg="white")
        listado_label.pack(pady=20)

    def mostrar_registrar_pago(self):
        # Limpiar el área principal y mostrar el formulario para registrar un nuevo pago
        for widget in self.content.winfo_children():
            widget.destroy()

        # Cargar y colocar el fondo
        registrar_frame = Image.open('images\\bg3.jpg')
        photo = ImageTk.PhotoImage(registrar_frame)
        registrar_frame_panel = tk.Label(self.content, image=photo)
        registrar_frame_panel.image = photo
        registrar_frame_panel.place(x=0, y=0, relwidth=1, relheight=1)

        # Colocar el texto encima del fondo
        registrar_label = tk.Label(self.content, text="Registrar Nuevo Pago", font=("Arial", 20), bg="white")
        registrar_label.pack(pady=20)

    def mostrar_generar_informes(self):
        # Limpiar el área principal y mostrar opciones para generar informes
        for widget in self.content.winfo_children():
            widget.destroy()

        # Cargar y colocar el fondo
        informes_frame = Image.open('images\\bg3.jpg')
        photo = ImageTk.PhotoImage(informes_frame)
        informes_frame_panel = tk.Label(self.content, image=photo)
        informes_frame_panel.image = photo
        informes_frame_panel.place(x=0, y=0, relwidth=1, relheight=1)

        # Colocar el texto encima del fondo
        informes_label = tk.Label(self.content, text="Generar Informes de Pagos", font=("Arial", 20), bg="white")
        informes_label.pack(pady=20)
        # Aquí puedes agregar opciones para seleccionar los tipos de informes a generar

# Para ejecutar la ventana de secretaria
def mostrar_pagina_secretaria():
    root = tk.Tk()
    app = SecretariaPage(root)
    root.mainloop()
