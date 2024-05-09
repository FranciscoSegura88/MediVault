import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class FormRegisterDesigner():

    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Registro de Usuario")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 500, 600)

        icono = tk.PhotoImage(file="./images/logo.png")
        self.ventana.iconphoto(True, icono)

        logo = utl.leer_imagen("./images/logo.png", (200, 200))

        # Frame del logo
        frame_logo = tk.Frame(self.ventana, bd=0, height=200, relief=tk.SOLID, padx=5, pady=2, bg="#F87474")
        frame_logo.pack(side="top", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg="#F87474")
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
        self.usuario.pack(fill=tk.X, padx=(0,20), pady=40)

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
        frame_confirmation.pack(fill=tk.X, padx=20, pady=5)

        etiqueta_confirmation = tk.Label(frame_confirmation, text="Confirmacion", font=('Arial', 14), bg='#fcfcfc')
        etiqueta_confirmation.pack(side="left", padx=(20,10), anchor="center", pady=4)
        self.confirmation = ttk.Entry(frame_confirmation, font=('Times', 14))
        self.confirmation.config(show="*")
        self.confirmation.pack(fill=tk.X, padx=20, pady=10)
        
        #TODO: Boton de Registrar
        register = tk.Button(frame_form, text="Registrar", font=('Arial', 15), bg='#F87474', bd=0, fg="#fff", command=self.register)
        register.pack(fill=tk.X, padx=1, pady=5)
        register.bind("<Return>", (lambda event: self.register()))
        
        self.ventana.mainloop()

    def register(self, event = None):
        pass