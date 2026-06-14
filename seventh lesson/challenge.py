class Rectangulo:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def area(self) -> float:
        return self.ancho * self.alto
    
    def perimetro(self) -> float:
        return (2 * self.ancho) + (2 * self.alto)
    

hola = Rectangulo(4, 3)
#print(hola.area())
#print(hola.perimetro())

class Termo:
    def __init__(self, capacidad: float, contenido: float):
        self.capacidad = capacidad
        self.contenido = 0.0

    def llenar(self, cantidad) -> float:
        suma = cantidad + self.contenido
        if suma > self.capacidad:
            raise ValueError("La cantidad no puede superar la capacidad del termo.")
        self.contenido = self.contenido + cantidad

    def vaciar(self) -> float:
        self.contenido = 0.0

termo = Termo(500, 200)
termo.llenar(200)
print(termo.contenido)
termo.llenar(200)
print(termo.contenido)
termo.llenar(200)
print(termo.contenido)