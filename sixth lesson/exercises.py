def potencia(base: float, exponente: int = 2) -> float:
    return base ** exponente

def contar_argumentos(*args):
    return len(args)

def mostrar_config(**kwargs) -> None:
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")