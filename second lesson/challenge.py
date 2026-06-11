#Parte B — código.
#  Crea una dataclass llamada Cliente con estos campos: nombre (texto), email (texto), y vip (booleano) que por defecto sea False.
#  Luego crea dos instancias: una usando el valor por defecto de vip, y otra marcándola como VIP. Imprime ambas.

from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    email: str
    vip: bool = False

one = Cliente(nombre = "Cristobal", email = "hola123@gmail.com")
two = Cliente(nombre = "XDD", email = "XDD@gmail.com", vip = True)
print(one,two)

#Parte C — encuentra el error.
#  El siguiente código está mal y Python lanzará un error al ejecutarlo.
#  Identifica cuál es el problema, explícame por qué falla, y escribe la versión corregida:

# CON ERROR
@dataclass
class Cuenta:
    saldo: float = 0.0
    titular: str
# CORREGIDO
@dataclass
class Cuenta:
    titular: str
    saldo: float = 0.0