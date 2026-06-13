def crear_saludo(nombre: str, idioma: str = "es") -> str:
    if idioma == "en":
        return f"Hello, {nombre}"
    elif idioma == "es":
        return f"Hola, {nombre}"
    
def multiplicar_todos(*numeros: float) -> float:
    total = 1
    for n in numeros:
        total = total * n
    return total

print(multiplicar_todos())

def construir_usuario(**datos) -> str | None:
    if "email" in datos:
        return datos
    else:
        raise ValueError("El Email es OBLIGATORIO") 
        



def construir_usuario(**datos) -> dict | None:
    for email, valor in datos.items():
        if email in datos:
            return datos
        else:
            raise ValueError("El Email es OBLIGATORIO") 