import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("MedVault")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg="#3a7ff6")
        self.ventana.resizable(width=0, height=0)
        
        icono = tk.PhotoImage(file="./images/logo.png")
        self.ventana.iconphoto(True, icono)

        logo = utl.leer_imagen("./images/logo.png", (200, 200))

        #frame del form con el background
        frame = tk.Frame(self.ventana, width=w, height=h, bd=0, bg="#3a7ff6")
        frame.pack()
        label = tk.Label(frame, image = logo, bg = "#3a7ff6")
        label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        #Nombre de la app
        appName_frame = tk.Frame(frame, bg="#3a7ff6")
        appName_frame.place(relx=0.5, rely=0.04, anchor="center")
        appName = tk.Label(appName_frame, text="MediVault", font=("Arial", 50), bg="#3a7ff6", fg="#fcfcfc")
        appName.pack(side="top", pady=5)

        #NSS
        nss_Frame = tk.Frame(frame, bg="#3a7ff6")
        nss_Frame.place(relx= 0.05, rely=0.1)
        nss_Label = tk.Label(nss_Frame, text="NSS:", font=("Arial", 30), bg="#3a7ff6", fg="#fcfcfc")
        nss_Label.pack(side="left", padx=(0,20))
        self.nss = ttk.Entry(nss_Frame, font=("Arial", 30))
        self.nss.pack(side="left", fill=tk.X, padx=(0, 20))
        #TODO: AGREGAR FUNCIONALIDAD AL BOTON
        tk.Button(nss_Frame, text="Buscar",font=("Arial", 19)).pack(side="left")

        self.ventana.mainloop()