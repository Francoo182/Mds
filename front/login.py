"""Importaciones varias"""
import tkinter as tk
from tkinter import messagebox
from frontend_utils import load_image, open_script  # Importar funciones desde el archivo utilitario
import requests
from PIL import Image, ImageTk
from doctora import mostrar_pagina_doctora
from profesional_page import mostrar_pagina_profesional
from secretaria_page import mostrar_pagina_secretaria

# Función para manejar el login
def login():
    email = entry_email.get()
    password = entry_password.get()

    # Hacer la petición a la API para autenticación
    url = f"http://127.0.0.1:8000/clients/login/{email}/{password}"  # Cambia a tu URL de la API
    data = {
        "email": email,
        "password": password
    }

    try:
        response = requests.get(url, json=data)

        if response.status_code == 200:
            result = response.json()
            rol = result.get("rol", "")  # Obtiene el rol, si existe
            if rol:
                print(f"Rol detectado: {rol}")
                messagebox.showinfo("Login Success", "Bienvenido")

                # Dependiendo del rol, abrir la ventana correspondiente
                if rol == "Doctora":
                    root.destroy()  # Cierra la ventana de login
                    mostrar_pagina_doctora()  # Llama a la función para abrir la ventana de Doctora
                elif rol == "Profesional":
                    root.destroy()
                    mostrar_pagina_profesional()
                   # abrir_ventana_profesional()  # Llama a la función para abrir la ventana de Profesional
                elif rol == "Secretaria":
                    root.destroy()
                    mostrar_pagina_secretaria()
                   # abrir_ventana_secretaria()  # Llama a la función para abrir la ventana de Secretaria
                else:
                    messagebox.showerror("Error", "Rol no reconocido.")
            else:
                print("No se encontró el campo 'rol' en la respuesta.")
        else:
            messagebox.showerror("Login Failed", "Correo o contraseña incorrectos")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo conectar a la API: {e}")
   
root = tk.Tk()
root.title("Login")
root.state('zoomed')  # Maximizar la ventana (sin ser pantalla completa)

#Cargar la imagen de fondo usando la función load_image() desde frontend_utils.py
bg_frame = load_image('fondo1.jpg')
if bg_frame:
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    bg_frame = bg_frame.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(bg_frame)

    # Crear el label para la imagen de fondo
    bg_panel = tk.Label(root, image=photo)
    bg_panel.image = photo  # Mantener la referencia de la imagen
    bg_panel.place(x=0, y=0, relwidth=1, relheight=1)  # Ajustar la imagen a toda la ventana

#Crear un frame para las etiquetas y campos de entrada
frame_login = tk.Frame(root, bg='pink', padx=40, pady=40)  # Aumento de padding para un frame más grande
frame_login.place(relx=0.5, rely=0.5, anchor='center')  # Centrar el frame en la ventana

#Etiquetas y campos de entrada dentro del frame
label_email = tk.Label(frame_login, text="Email", bg='pink')  # Fondo rosado para la etiqueta
label_email.pack(pady=(0, 10))  # Padding inferior de 10

entry_email = tk.Entry(frame_login)
entry_email.pack(pady=(0, 20))  # Padding inferior de 20

label_password = tk.Label(frame_login, text="Password", bg='pink')  # Fondo rosado para la etiqueta
label_password.pack(pady=(0, 10))

entry_password = tk.Entry(frame_login, show="*")  # Oculta el texto para el password
entry_password.pack(pady=(0, 20))  # Padding inferior de 20

#Botón de Login
button_login = tk.Button(frame_login, text="Login", command=login)
button_login.pack(pady=(0, 10))  # Padding inferior de 10

#Crear el botón de registro que abre register.py utilizando la función open_script()
button_signup = tk.Button(frame_login, text="Registrarse", command=lambda: open_script('register.py'))
button_signup.pack()

# Correr la interfaz de Tkinter
root.mainloop()

