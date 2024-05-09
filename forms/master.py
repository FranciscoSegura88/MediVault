import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

class App:

    def cerrar_sesion(self):
        self.ventana.destroy()
        from forms.login import Login_Form
        Login_Form()

    def exitFullScreen(self, event):
        self.ventana.attributes("-fullscreen", False)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.attributes("-fullscreen", True)
        self.ventana.bind("<Escape>", self.exitFullScreen)

        # Carga de la imagen de fondo
        self.background_image = Image.open("./images/logo.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        
        # Creamos un label para la imagen de fondo
        self.background_label = tk.Label(self.ventana, image=self.background_photo, bg = "#fcfcfc")
        self.background_label.place(relwidth=1, relheight=1)

        # Creación del frame principal
        frame = tk.Frame(self.ventana, bg = "#fcfcfc")
        frame.place( relx=0.12, rely=0.07, anchor=tk.CENTER)

        # Etiqueta y campo de entrada
        etiqueta_nss = tk.Label(frame, text="NSS", font=("Arial", 14), bg="#fcfcfc", bd = 0)
        etiqueta_nss.grid(row=0, column=0, padx=(20,10), pady=40)
        self.nss = ttk.Entry(frame, font=("Arial", 14), background="#fcfcfc")
        self.nss.grid(row=0, column=1, padx=(0,10), pady=40)
        buscar = tk.Button(frame, text = "Buscar", font = ("Arial", 14), bg = "#fcfcfc")
        buscar.grid(row=0, column=2)

        # Etiqueta y botón de "cerrar sesión"
        etiqueta_cerrarsesion = tk.Button(self.ventana, text="Cerrar Sesión", font=("Arial", 15), bg = "#fcfcfc", command = self.cerrar_sesion)
        etiqueta_cerrarsesion.place(relx= 0.9, rely= 0.9)

        self.ventana.mainloop()

