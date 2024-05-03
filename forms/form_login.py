import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel

class App:

    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        if(usu == "root" and password == "1234"):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="El usuario o contraseña no son correctos", title = "Error")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("500x600")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 500, 600)

        logo = utl.leer_imagen("./images/logo.png", (200, 200))

        # Frame del logo
        frame_logo = tk.Frame(self.ventana, bd=0, height=200, relief=tk.SOLID, padx=5, pady=2, bg="#ffd700")
        frame_logo.pack(side="top", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg="#ffd700")
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
        
        #Boton inicio de Sesion
        inicio = tk.Button(frame_form, text = "Iniciar sesion", font = ("Arial", 18, BOLD), bg = "#008000", command = self.verificar)
        inicio.pack(padx= 5, pady= 25)
        #TODO: No esta funcionando darle enter
        inicio.bind("<Return>", (lambda event: self.verificar()))

        self.ventana.mainloop()

app = App()
