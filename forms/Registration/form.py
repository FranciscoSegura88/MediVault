from forms.Registration.form_designer import FormRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_User
from tkinter import messagebox
import util.encoding_decoding as end_dec
import tkinter as tk

class FormRegister(FormRegisterDesigner):
    
    def __init__(self):
        super().__init__()