from sqlalchemy import create_engine, Column, Integer, String, Date, Time, Text, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Auth_User(Base):
    __tablename__ = 'auth_user'

    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(50), nullable=False, unique=True)
    contrasena = Column(String(50), nullable=False)
    tipo_usuario = Column(Enum('Admin', 'Medico', 'Paciente'), nullable=False)

    
class Hospital(Base):
    __tablename__ = 'hospital'

    id_hospital = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(100), nullable=False)
    telefono = Column(String(12), nullable=False)
    correo_electronico = Column(String(30))

class Medico(Base):
    __tablename__ = 'medico'

    RFC = Column(String(12), primary_key=True)
    id_hospital = Column(Integer, ForeignKey('hospital.id_hospital'))
    nombre = Column(String(50), nullable=False)
    genero = Column(Enum('Hombre', 'Mujer'), nullable=True)
    fecha_nacimiento = Column(Date, nullable=False)
    correo_electronico = Column(String(80))
    especialidad = Column(String(40), nullable=False)
    consulta = Column(Integer)
    hospital = relationship("Hospital", back_populates="medicos")

class Paciente(Base):
    __tablename__ = 'paciente'

    numero_sc = Column(String(11), primary_key=True)
    id_seguro = Column(Integer, ForeignKey('seguro.id_seguro'))
    nombre = Column(String(50), nullable=False)
    telefono = Column(String(12), nullable=False)
    direccion = Column(String(100), nullable=False)
    correo_electronico = Column(String(30))
    genero = Column(Enum('Hombre', 'Mujer', 'No Binario'))
    fecha_nacimiento = Column(Date, nullable=False)
    seguro = relationship("Seguro", back_populates="pacientes")

class Cita(Base):
    __tablename__ = 'cita'

    id_cita = Column(Integer, primary_key=True)
    numero_sc = Column(String(12), ForeignKey('paciente.numero_sc'))
    RFC = Column(String(12), ForeignKey('medico.RFC'))
    fecha = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)
    paciente = relationship("Paciente", back_populates="citas")
    medico = relationship("Medico", back_populates="citas")

class Diagnostico(Base):
    __tablename__ = 'diagnostico'

    id_diagnostico = Column(Integer, primary_key=True)
    id_prueba = Column(Integer, ForeignKey('prueba.id_prueba'))
    descripcion = Column(Text, nullable=False)
    comentarios = Column(Text, nullable=False)
    prueba = relationship("Prueba", back_populates="diagnosticos")

class HistorialClinico(Base):
    __tablename__ = 'historial_clinico'

    numero_sc = Column(String(12), ForeignKey('paciente.numero_sc'), primary_key=True)
    paciente = relationship("Paciente", back_populates="historial")

class Prueba(Base):
    __tablename__ = 'prueba'

    id_prueba = Column(Integer, primary_key=True)
    numero_sc = Column(String(12), ForeignKey('paciente.numero_sc'))
    nombre_prueba = Column(Text, nullable=False)
    fecha_prueba = Column(Date, nullable=False)
    resultado = Column(Text, nullable=False)
    paciente = relationship("Paciente", back_populates="pruebas")
    diagnosticos = relationship("Diagnostico", back_populates="prueba")

class Seguro(Base):
    __tablename__ = 'seguro'

    id_seguro = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    pacientes = relationship("Paciente", back_populates="seguro")

class Tratamiento(Base):
    __tablename__ = 'tratamiento'

    id_tratamiento = Column(Integer, primary_key=True)
    id_diagnostico = Column(Integer, ForeignKey('diagnostico.id_diagnostico'))
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    descripcion = Column(Text, nullable=False)
    comentarios = Column(Text, nullable=False)
    diagnostico = relationship("Diagnostico", back_populates="tratamientos")


