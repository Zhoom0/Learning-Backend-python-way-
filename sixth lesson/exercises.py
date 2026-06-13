def potencia(base: float, exponente: int = 2) -> float:
    return base ** exponente

def contar_argumentos(*args):
    return len(args)

print(contar_argumentos(1, 190823, "hola", True))