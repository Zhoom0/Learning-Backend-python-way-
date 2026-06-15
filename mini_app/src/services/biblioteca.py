from models.libro import Libro


def libros_disponibles(libros: list[Libro]) -> list[Libro]:
    return [l for l in libros if l.disponible]