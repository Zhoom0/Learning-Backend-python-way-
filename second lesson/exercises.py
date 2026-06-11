from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int



    #Ejercicio 1 (sin respuesta). Convierte esta clase normal en una dataclass equivalente:
class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

@dataclass
class Libro:
    titulo: str
    autor: str
    paginas: int

    # Ejercicio 2 (sin respuesta).
    # Crea una dataclass Pedido con un campo id (entero), un campo total (decimal),
    # y un campo pagado (booleano) que por defecto sea False.

@dataclass
class Pedido:
    id: int
    total: float
    pagado: bool = False