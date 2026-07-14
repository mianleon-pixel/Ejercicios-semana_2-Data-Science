numeros = [4, 7, 2, 4, 9, 7, 1, 2, 10, 4]
# 2. Creamos una lista vacía para guardar los números únicos
unicos = []
for n in numeros:
    if n not in unicos:
        unicos.append(n)
print("Lista sin duplicados:", unicos)