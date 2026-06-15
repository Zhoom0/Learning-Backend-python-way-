from dataclasses import dataclass

@dataclass
class Libro:
    titulo: str
    autor: str
    disponible: bool = True