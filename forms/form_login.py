import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry("500x600")
        self.ventana.config(bg = "#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 500, 600)
        
        logo = utl.leer_imagen("./images/logo.png", (200, 200))

        #TOP
        frame_logo = tk.Frame(self.ventana, bd = 0, height= 200, relief = tk.SOLID, padx = 5, pady = 2, bg = "#ffd700")
        frame_logo.pack(side = "top", expand = tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg="#ffd700")
        label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        #Crea frame a la derecha
        frame_form = tk.Frame(self.ventana, bd = 0, relief = tk.SOLID, bg = "#470501")
        frame_form.pack(side = "bottom", expand = tk.YES, fill = tk.BOTH)

        frame_form_bottom = tk.Frame(frame_form, height = 300, bd = 0, relief = tk.SOLID, bg = "#470501")
        frame_form_bottom.pack(side = "top", fill = tk.BOTH)
        title = tk.Label(frame_form_bottom, text = "Inicio de Sesion", font=("Arial", 30), bg="#470501", pady=10, fg="#fcfcfc")
        title.pack(expand = tk.YES, fill = tk.BOTH)

        

        self.ventana.mainloop()

app = App()