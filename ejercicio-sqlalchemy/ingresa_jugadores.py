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

# leer el archivo de establecimientos

archivo = open("data/mundial2018.csv", "r", encoding="utf-8")

leer_archivo = archivo.readlines()

# Eliminar el encabezado del CSV
leer_archivo.pop(0)

for jugador in leer_archivo:

    # Separar el string en un arreglo
    jugador_array = jugador.split("|")

    # Ingresar los datos del CSV en la base de datos en la entidad jugador
    j = Jugador(    numero = jugador_array[0], 
                    FIFADisplayName = jugador_array[1], 
                    pais = jugador_array[2],
                    apellido = jugador_array[3],
                    nombre = jugador_array[4],
                    shirtName = jugador_array[5],
                    pos = jugador_array[6],
                    altura = jugador_array[7],
                    caps = jugador_array[8],
                    goles = jugador_array[9])
    session.add(j)

session.commit()