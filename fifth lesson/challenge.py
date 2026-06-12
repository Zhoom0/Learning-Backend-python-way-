salarios = [800000, 1200000, 1500000, 2000000]
aumento = [n * 1.1 for n in salarios]


palabras = ["python", "go", "java", "rust", "c", "javascript"]
transformation = [c.upper() for c in palabras if len(c) > 3]
print(transformation)


numeros = [1, 2, 3, 4, 5]
pares = {n: n % 2 == 0 for n in numeros}
print(pares)