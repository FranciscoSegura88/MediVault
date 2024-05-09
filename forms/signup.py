import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import sqlite3

class Signup_Form:

    def regresar(self):
        self.ventana.destroy()

    def registrar_usuario(self):
        try:
            # Conectar a la base de datos
            with sqlite3.connect("./db/usuarios.db") as conexion:
                cursor = conexion.cursor()

                # Verificar si el campo de usuario está en blanco
                if not self.usuario.get():
                    messagebox.showerror("Error", "El campo de usuario no puede estar en blanco")
                    return

                # Verificar si las contraseñas coinciden
                if self.password.get() != self.confirmation.get():
                    messagebox.showerror("Error", "Las contraseñas no coinciden")
                    return

                # Verificar si el usuario ya existe
                usuario = self.usuario.get()
                cursor.execute("SELECT usuario FROM usuarios WHERE usuario=?", (usuario,))
                existe = cursor.fetchone()
                if existe:
                    messagebox.showerror("Error", f"El usuario '{usuario}' ya existe. Por favor, elija otro nombre de usuario.")
                    return

                # Insertar nuevo usuario en la base de datos
                contraseña = self.password.get()
                cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contraseña))
                conexion.commit()

                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                self.ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Registro de Usuario")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        self.ventana.geometry("500x600")

        icono = tk.PhotoImage(file="./images/logo.png")
        self.ventana.iconphoto(True, icono)

        banner = ImageTk.PhotoImage(Image.open("./images/logo.png").resize((200,200)))
        self.ventana.iconphoto(True, banner)

        # Frame del logo
        frame_logo = tk.Frame(self.ventana, bd=0, height=200, relief=tk.SOLID, padx=5, pady=2, bg="#F87474")
        frame_logo.pack(side="top", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=banner, bg="#F87474")
        label.pack(fill=tk.BOTH, expand=True)

        # Frame del formulario
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        # Frame del texto "Registro de Usuario"
        frame_form_text = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form_text.pack(side="top", fill=tk.BOTH)
        title = tk.Label(frame_form_text, text="Registro de usuario", font=("Arial", 30), bg="#fcfcfc", pady=10)
        title.pack(fill=tk.BOTH, expand=True)

        # Frame del entry de usuario
        frame_usuario = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_usuario.pack(fill=tk.X, padx=20, pady=5)
        etiqueta_usuario = tk.Label(frame_usuario, text="Usuario", font=("Arial", 14), bg="#fcfcfc")
        etiqueta_usuario.pack(side="left", padx=(20,10), anchor="center", pady=4)
        self.usuario = ttk.Entry(frame_usuario, font=("Arial", 14))
        self.usuario.pack(fill=tk.X, padx=(0,20), pady=20)

        # Frame del entry de la contraseña
        frame_password = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_password.pack(fill=tk.X, padx=20, pady=5)
        etiqueta_password = tk.Label(frame_password, text="Contraseña", font=("Arial", 14), bg="#fcfcfc")
        etiqueta_password.pack(side="left", padx=(20,10), anchor="center", pady=4)
        self.password = ttk.Entry(frame_password, font=("Arial", 14))
        self.password.config(show="*")
        self.password.pack(fill=tk.X, padx=(0,20))  
        
        # Frame del entry de la Confirmation
        frame_confirmation = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_confirmation.pack(fill=tk.X, padx=10, pady=5)
        etiqueta_confirmation = tk.Label(frame_confirmation, text="Confirmacion", font=('Arial', 14), bg='#fcfcfc')
        etiqueta_confirmation.pack(side="left", padx=(20,10), anchor="center", pady=4)
        self.confirmation = ttk.Entry(frame_confirmation, font=('Times', 14))
        self.confirmation.config(show="*")
        self.confirmation.pack(fill=tk.X, padx=20, pady=10)
        
        # Boton de Registrar
        registrar = tk.Button(frame_form, text="Registrar", font=("Arial", 18), bg="#F87474", command=self.registrar_usuario)
        registrar.pack()
        self.ventana.bind("<Return>", lambda event: self.registrar_usuario())

        # Botón para abrir el formulario de registro
        regreso = tk.Button(frame_form, text="Iniciar sesión", font=("Arial", 15), bg="#fcfcfc", bd=0, fg="#F87474", command=self.regresar)
        regreso.pack(padx=1, pady=5)

        self.ventana.mainloop()