lista1 = [4, 8, 12, 16, 20]
lista2 = [8, 10, 12, 18, 20]
unicos = []
for n in lista1:
    if n not in lista2:
        unicos.append(n)
for n in lista2:
    if n not in lista1:
        unicos.append(n)
print("Elementos únicos entre ambas listas:", unicos)