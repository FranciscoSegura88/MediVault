import sqlalchemy as db
from persistence.model import Auth_User
from sqlalchemy.orm import Session
from tkinter import ttk

class AuthUserRepository():
    def __init__(self):
        self.engine = db.create_engine('sqlite:///db/login.sqlite', echo = False, future = True)

    def getUserByUserName(self, user_name: str):
        try:
            with Session(self.engine) as session:
                user = session.query(Auth_User).filter_by(nombre_usuario=user_name).first()
                return user
        except Exception as e:
            ttk.showmessageerror(text="Error al obtener el usuario: {e}")
            return None
        
    def insertUser(self, user: Auth_User):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()