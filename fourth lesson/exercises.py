#Ejercicio 1 (sin respuesta).
#  Protege este código con try/except para que, si la conversión falla, imprima "Entrada inválida" en vez de caerse:
"""
valor = int("treinta")
print(valor)
"""
try:
    valor = int("treinta")
    print(valor)
except ValueError:
    print("La conversión falló.")

#Ejercicio 2 (sin respuesta).
#  Escribe una función raiz_segura(n) que devuelva la raíz cuadrada de n (usa math.sqrt),
#  pero que si n es negativo lance un ValueError con el mensaje "No existe raíz de números negativos".}
#  (Recuerda importar math.)
import math

def raiz_segura(n: float) -> float:
    if n < 0:
        raise ValueError("No existe raíz de números negativos")
    return math.sqrt(n)