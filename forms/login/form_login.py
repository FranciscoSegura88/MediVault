import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import FormLoginDesigner
from persistence.model import Auth_User
import util.encoding_decoding as end_dec
from persistence.repository.auth_user_repository import AuthUserRepository
from forms.Registration.form import FormRegister

class FormLogin(FormLoginDesigner):

    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()

    def verificar(self):
        user_db: Auth_User = self.auth_repository.getUserByUserName(self.usuario.get())
        if self.isUser(user_db):
            self.isPassword(self.password.get(), user_db)

    def userSignup(self):
        FormRegister().mainloop()

    def isUser(self, user: Auth_User):
        if user is None:
            messagebox.showerror(message="El usuario no existe, favor de registrarse", title="Mensaje")
            return False
        return True

    #def isPassword(self, password: str, user: Auth_User):
        b_password = end_dec.decrypt(user.password).decode("utf-8")
        if password == b_password:
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")

    def isPassword(self, password, user_db):
        if user_db is None:
            ttk.showmessageerror(text="Usuario no encontrado")
        else:
            b_password = password  # Just to avoid using password before defining it
            if user_db is not None:
                b_password = end_dec.decrypt(user_db.password).decode("utf-8")
            if password == b_password:
                self.ventana.destroy()
                self.openMainWindow(user_db)
            else:
                ttk.showmessageerror(text="Contraseña incorrecta")

