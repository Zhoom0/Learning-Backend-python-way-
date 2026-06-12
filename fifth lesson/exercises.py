temperaturas = [12, 18, 25, 30, 8]
fahrenheit = [c * 9/5 + 32 for c in temperaturas]
print(fahrenheit)


numeros = [4, 7, 10, 13, 16, 20]
multiplos = [n for n in numeros if n % 4 == 0]
print(multiplos)


productos = ["pan", "leche", "huevos"]
stock = {producto: len(producto) for producto in productos}
print(stock)