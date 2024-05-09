from forms.Registration.form_designer import FormRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_User
from tkinter import messagebox
import util.encoding_decoding as end_dec
import tkinter as tk

class FormRegister(FormRegisterDesigner):
    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()

    def register(self):
        if self.isConfirmationPassword():
            if not self.isUserRegistered(self.usuario.get()):
                user = Auth_User()
                user.nombre_usuario = self.usuario.get()
                user.contrasena = end_dec.encrypted(self.password.get())
                self.auth_repository.insertUser(user)
                messagebox.showinfo(message="Se registró el usuario", title="Mensaje")
                self.ventana.destroy()

    def isConfirmationPassword(self):
        status = True
        if self.password.get() != self.confirmation.get():
            status = False
            messagebox.showerror(message="Las contraseñas no coinciden", title="Mensaje")
            self.password.delete(0, tk.END)
            self.confirmation.delete(0, tk.END)
        return status
    
    def isUserRegistered(self, username):
        user = self.auth_repository.getUserByUserName(username)
        if user:
            messagebox.showerror(message="El usuario ya existe", title="Mensaje")
            return True
        return False