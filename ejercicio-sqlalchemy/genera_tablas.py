from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Jugador(Base):
    __tablename__ = 'jugador'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    FIFADisplayName = Column(String(50))
    pais = Column(String(50))
    apellido = Column(String(50))
    nombre = Column(String(50))
    shirtName = Column(String(50))
    pos = Column(String(50))
    altura = Column(Integer)
    caps = Column(Integer)
    goles = Column(Integer)

    def __repr__(self):
        return "Jugador:\nNumero = %s - FIFADisplayName = %s - Pais = %s - Apellido = %s - Nombre = %s - ShirtName = %s - Posicion = %s - Altura = %s - Caps = %s - Goles = %s\n" % (
                          self.numero, 
                          self.FIFADisplayName, 
                          self.pais, 
                          self.apellido, 
                          self.nombre, 
                          self.shirtName, 
                          self.pos, 
                          self.altura, 
                          self.caps, 
                          self.goles)

Base.metadata.create_all(engine)
