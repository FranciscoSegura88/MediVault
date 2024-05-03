import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import FormLoginDesigner

class FormLogin(FormLoginDesigner):

    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        if(usu == "root" and password == "1234"):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="El usuario o contraseña no son correctos", title = "Error")

    def __init__(self):
        super().__init__()
