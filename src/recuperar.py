from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.album import Album, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    # Crear la sesión
    session = Session()

    # Recuperar todas las canciones
    canciones = session.query(Cancion).all()

    print('Las canciones almacenadas son:')
    for cancion in canciones:
        print("Título: " + cancion.titulo + " (00:" +
              str(cancion.minutos) + ":" +
              str(cancion.segundos) + ")")

        print("Intérpretes:")
        for interprete in cancion.interpretes:
            print(" - " + interprete.nombre)

        for album in cancion.albumes:
            print(" -- Presente en el álbum: " + album.titulo)

        print("")

    # Filtrar y mostrar álbumes almacenados en discos
    print('Los álbumes almacenados en discos son:')
    albumes = session.query(Album).filter(Album.medio == Medio.DISCO).all()
    for album in albumes:
        print("Álbum: " + album.titulo)

    # Cerrar la sesión
    session.close()
