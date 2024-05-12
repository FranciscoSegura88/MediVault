from cryptography.fernet import Fernet

class Seguridad:

    clave = b'tUx7n_Rbsi3S6zZR_zK23y9tAsqlP45TE5Q0rhXyUEA='

    @staticmethod
    def encriptar(password: str):
        f = Fernet(Seguridad.clave)
        password_bytes = password.encode('utf-8')
        password_encriptada = f.encrypt(password_bytes)
        return password_encriptada

    @staticmethod
    def desencriptar(password_encriptada: bytes):
        f = Fernet(Seguridad.clave)
        password_bytes = f.decrypt(password_encriptada)
        password = password_bytes.decode('utf-8')
        return password
