#Parte B — código.
#  Escribe una función convertir_a_entero(texto: str) que intente convertir el texto a entero y lo devuelva.
#  Si la conversión falla, debe atrapar el error e imprimir "No se pudo convertir" y devolver None.
#  Anota bien el tipo de retorno (piensa: a veces devuelve un entero, a veces None).

def convertir_a_entero(texto: str) -> int | None:
    try:
        return int(texto)
    except ValueError:
        print("No se pudo convertir.")
        return None


#Parte C — usa raise.
#  Escribe una función validar_edad(edad: int)
#  que lance un ValueError con un mensaje claro si la edad es menor que 0 o mayor que 150 (ninguna edad real está fuera de ese rango).
#  Si la edad es válida, que la devuelva. (Pista: puedes comprobar ambas condiciones inválidas.)

def validar_edad(edad: int) -> int:
    if 0 <= edad <= 150:
        return edad
    if edad > 150:
        raise ValueError("Ingresa un numero menor a 150.")
    if edad < 0:
        raise ValueError("Ingresa un numero mayor a 0.")
    
#Parte D — encuentra el error.
#  Este código intenta manejar un error pero está mal pensado: no atrapa el tipo de excepción correcto, así que igual se va a caer.
#  Dime qué excepción se lanzará en realidad, por qué el except actual no la atrapa, y escribe la versión corregida:
try:
    datos = {"nombre": "Ana"}
    print(datos["edad"])
except ValueError:
    print("No se encontró la clave")

# R: Se debe utilizar un KeyError.

try:
    datos = {"nombre": "Ana"}
    print(datos["edad"])
except KeyError:
    print("No se encontró la clave")