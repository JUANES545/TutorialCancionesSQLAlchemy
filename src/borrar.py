from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.album import Album, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    # Crear la sesión
    session = Session()

    # Recuperar la canción con id 2 usando Session.get()
    cancion2 = session.get(Cancion, 2)

    if cancion2:
        # Borrar la canción
        session.delete(cancion2)

        # Confirmar los cambios en la base de datos
        session.commit()

    # Cerrar la sesión
    session.close()
