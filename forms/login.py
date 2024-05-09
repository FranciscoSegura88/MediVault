import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import sqlite3
from forms.signup import Signup_Form
from forms.master import App

class Login_Form:

    def userSignup(self):
        Signup_Form()

    def verificar(self):
        try:
            # Conectar a la base de datos
            with sqlite3.connect("./db/usuarios.db") as conexion:
                cursor = conexion.cursor()

                # Verificar si el usuario existe
                usuario = self.usuario.get()
                contraseña = self.password.get()
                cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
                resultado = cursor.fetchone()

                if resultado:
                    # Verificar la contraseña
                    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?", (usuario, contraseña))
                    resultado = cursor.fetchone()
                    if resultado:
                        self.ventana.destroy()
                        App()
                    else:
                        messagebox.showerror("Error", "Contraseña incorrecta")
                else:
                    # Crear nuevo usuario
                    respuesta = messagebox.askquestion("Usuario no encontrado", "El usuario no existe, ¿desea registrarse?")
                    if respuesta == "yes":
                        Signup_Form()
                    else:
                        messagebox.showinfo("Información", "Puede registrarse cuando lo desee")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("MedVault")
        self.ventana.geometry("500x600")
        self.ventana.resizable(width=0, height=0)

        banner = ImageTk.PhotoImage(Image.open("./images/logo.png").resize((200,200)))
        self.ventana.iconphoto(True, banner)
            
        # Frame del logo
        frame_logo = tk.Frame(self.ventana, bd=0, height=50, relief=tk.SOLID, padx=5, pady=2, bg="#ffd700")
        frame_logo.pack(side="top", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=banner, bg="#ffd700")
        label.pack(fill=tk.BOTH, expand=True)

        # Frame del formulario
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        # Frame del texto "inicio de sesión"
        frame_form_text = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form_text.pack(side="top", fill=tk.BOTH)
        title = tk.Label(frame_form_text, text="Inicio de Sesión", font=("Arial", 30), bg="#fcfcfc", pady=10)
        title.pack(fill=tk.BOTH, expand=True)

        # Frame del entry de usuario
        frame_usuario = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_usuario.pack(fill=tk.X, padx=20, pady=5)
        etiqueta_usuario = tk.Label(frame_usuario, text="Usuario", font=("Arial", 14), bg="#fcfcfc")
        etiqueta_usuario.pack(side="left", padx=(20,10), anchor="center", pady=40)
        self.usuario = ttk.Entry(frame_usuario, font=("Arial", 14))
        self.usuario.pack(fill=tk.X, padx=(0,20), pady=40)

        # Frame del entry de la contraseña
        frame_password = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_password.pack(fill=tk.X, padx=20, pady=5)
        etiqueta_password = tk.Label(frame_password, text="Contraseña", font=("Arial", 14), bg="#fcfcfc")
        etiqueta_password.pack(side="left", padx=(20,10), anchor="center", pady=4)
        self.password = ttk.Entry(frame_password, font=("Arial", 14))
        self.password.config(show="*")
        self.password.pack(fill=tk.X, padx=(0,20))
        
        # Botón inicio de Sesión
        inicio = tk.Button(frame_form, text="Iniciar sesión", font=("Arial", 18), bg="#ffd700", command=self.verificar)
        inicio.pack(padx=5, pady=15)
        self.ventana.bind("<Return>", (lambda event: self.verificar()))  # Para ejecutar la verificación al presionar "Enter"

        # Botón para abrir el formulario de registro
        registro = tk.Button(frame_form, text="Registrar usuario", font=("Arial", 15), bg="#fcfcfc", bd=0, fg="#3a7ff6", command=self.userSignup)
        registro.pack(padx=1, pady=5)

        self.ventana.mainloop()