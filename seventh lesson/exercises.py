class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
    
    def descripcion(self) -> str:
        return f"{self.titulo} hecho por {self.autor}"


libro = Libro("Clases y metodos", "Cristobal")

print(libro.titulo)
print(libro.descripcion())


class Lampara:
    def __init__(self, encendida):
        self.encendida = False

    def encender(self):
        if self.encendida == True:
            raise ValueError("La lampara ya está encendida.")
        self.encendida = True

    def apagar(self):
        if self.encendida == False:
            raise ValueError("La lampara ya está apagada.")
        self. encendida = False