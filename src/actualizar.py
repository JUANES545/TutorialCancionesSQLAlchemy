from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    # Crear la sesión
    session = Session()

    # Recuperar la canción con id 2 y el intérprete con id 4
    cancion = session.query(Cancion).get(2)
    interprete = session.query(Interprete).get(4)

    # Actualizar los atributos de la canción
    cancion.minutos = 5
    cancion.segundos = 30
    cancion.compositor = "Pedro Pérez"

    # Añadir el intérprete a la canción
    cancion.interpretes.append(interprete)

    # Añadir la canción actualizada a la sesión
    session.add(cancion)

    # Confirmar los cambios en la base de datos
    session.commit()

    # Cerrar la sesión
    session.close()
