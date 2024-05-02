import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
#Dios, porfavor dame la paciencia y el conocimiento del porque putas madres esta dando error este import si el hijo de puta directorio
#esta en la misma maldita carpeta y tiene el puto nombre del archivo.py, porfavor Dios ayudame 
import util.generic as utl
from forms.form_master import MasterPanel

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry("800x500")
        self.ventana.config(bg = "#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana)

        self.ventana.mainloop()