from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los jugadores, ordenados por la estatura..

print("--------------------------------")
jugadores = session.query(Jugador).order_by(Jugador.altura).all()
print(jugadores)