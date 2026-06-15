from models.libro import Libro
from services.biblioteca import libros_disponibles



l1 = Libro(
   titulo = "lol",
   autor = "cristobal",
   disponible = True
)

l2 = Libro(
   titulo = "loool",
   autor = "cristobal2",
   disponible = True
)

l3 = Libro(
   titulo = "XDD",
   autor = "cristoba3",
   disponible = False
)
libritos = [l1, l2, l3]
if __name__ == "__main__":
    print(libros_disponibles(libritos))