#Ejercicio 1 (sin respuesta).
#Anota esta función: recibe el nombre de un producto (texto) y su precio (decimal), y devuelve un texto.

def describir_producto(nombre: str, precio: float) -> str:
    return f"{nombre} cuesta ${precio}"


#Ejercicio 2 (sin respuesta).
#Anota esta función: recibe una lista de edades (enteros) y devuelve el promedio (decimal).

def edad_promedio(edades:list [int]) -> float:
    return sum(edades) / len(edades)


def aplicar_descuento(precio: float, descuento: int) -> float:
    return (precio * (100 - descuento)) / 100


def buscar_precio(precios: dict[str, float], buscar: str) -> float | None:
    return precios.get(buscar)