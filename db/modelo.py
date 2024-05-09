import sqlite3

# Función para crear la base de datos y las tablas
def create_database():
    try:
        conn = sqlite3.connect('medvault.db')
        cursor = conn.cursor()

        # Crear tabla hospital
        cursor.execute('''CREATE TABLE IF NOT EXISTS hospital (
                          id_hospital INTEGER PRIMARY KEY AUTOINCREMENT,
                          nombre TEXT NOT NULL,
                          direccion TEXT NOT NULL,
                          telefono TEXT NOT NULL,
                          correo_electronico TEXT)''')

        # Crear tabla medico
        cursor.execute('''CREATE TABLE IF NOT EXISTS medico (
                          RFC TEXT PRIMARY KEY,
                          id_hospital INTEGER,
                          nombre TEXT NOT NULL,
                          genero TEXT CHECK (genero IN ('Hombre', 'Mujer')),
                          fecha_nacimiento DATE CHECK (fecha_nacimiento BETWEEN '1900-01-01' AND '2100-01-01'),
                          correo_electronico TEXT,
                          especialidad TEXT NOT NULL,
                          consulta INTEGER,
                          FOREIGN KEY (id_hospital) REFERENCES hospital(id_hospital))''')

        # Crear tabla paciente
        cursor.execute('''CREATE TABLE IF NOT EXISTS paciente (
                          numero_sc TEXT PRIMARY KEY,
                          nombre TEXT NOT NULL,
                          genero TEXT CHECK (genero IN ('Hombre', 'Mujer')),
                          fecha_nacimiento DATE CHECK (fecha_nacimiento BETWEEN '1900-01-01' AND '2100-01-01'),
                          correo_electronico TEXT,
                          telefono TEXT NOT NULL)''')

        # Crear tabla historial_clinico
        cursor.execute('''CREATE TABLE IF NOT EXISTS historial_clinico (
                          id_historial INTEGER PRIMARY KEY AUTOINCREMENT,
                          numero_sc TEXT,
                          FOREIGN KEY (numero_sc) REFERENCES paciente(numero_sc))''')

        # Crear tabla cita
        cursor.execute('''CREATE TABLE IF NOT EXISTS cita (
                          id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
                          numero_sc TEXT,
                          RFC TEXT,
                          fecha DATE NOT NULL,
                          horario TIME NOT NULL,
                          FOREIGN KEY (numero_sc) REFERENCES paciente(numero_sc),
                          FOREIGN KEY (RFC) REFERENCES medico(RFC))''')

        # Crear tabla prueba
        cursor.execute('''CREATE TABLE IF NOT EXISTS prueba (
                          id_prueba INTEGER PRIMARY KEY AUTOINCREMENT,
                          tipo_prueba TEXT NOT NULL)''')

        # Crear tabla diagnostico
        cursor.execute('''CREATE TABLE IF NOT EXISTS diagnostico (
                          id_diagnostico INTEGER PRIMARY KEY AUTOINCREMENT,
                          id_prueba INTEGER,
                          descripcion TEXT NOT NULL,
                          comentarios TEXT NOT NULL,
                          FOREIGN KEY (id_prueba) REFERENCES prueba(id_prueba))''')

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"No se pudo crear la base de datos: {e}")

# Llamar a la función para crear la base de datos y las tablas
create_database()
