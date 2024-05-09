import sqlite3

def crear_base_de_datos():
    # Conectar a la base de datos (creará la base de datos si no existe)
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    # Crear tabla de usuarios si no existe
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        usuario TEXT,
                        contraseña TEXT
                    )""")
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_base_de_datos()
    print("Base de datos creada exitosamente")
