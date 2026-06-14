class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
    
    def descripcion(self) -> str:
        return f"{self.titulo} hecho por {self.autor}"


libro = Libro("Clases y metodos", "Cristobal")

print(libro.titulo)
print(libro.descripcion())