from cryptography import fernet

def encrypted(password:str):
    f = fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    b_password = bytes(password, 'ascii')
    encrypted_password = f.encrypt(b_password)
    return encrypted_password.decode('ascii')

def decrypt(password:str):
    f = fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    b_password = bytes(password, 'ascii')
    b_password_decrypt = f.decrypt(b_password)
    return b_password_decrypt.decode('ascii')