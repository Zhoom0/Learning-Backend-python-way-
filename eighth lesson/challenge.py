from typing import Optional, Union

#def procesar(dato: Union[int, str], extra: Optional[float]) -> Optional[str]:

#def procesar(dato : int | str, extra: float | None) -> str | None:




def buscar_usuario(usuarios: list[dict[str, str]], email: str) -> dict[str, str] | None:
    for e in usuarios:
        if e.get("email") == email:
            return e
    return None

correo: str = "hola123@gmail.com"
correo2: str = "chao321@gmail.com"

database: list[dict[str, str]] = [
    {"nombre": "Cristobal", "ciudad": "Concepción", "email": correo},
    {"nombre": "Matías", "ciudad": "Concepción", "email": correo2}
]

