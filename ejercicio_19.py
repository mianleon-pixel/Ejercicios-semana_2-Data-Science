numeros = [1, 2, 3, 4]
letras = ['a', 'b', 'c', 'd']
combinada = []
for n, l in zip(numeros, letras):
    combinada.append(n)
    combinada.append(l)
print("Lista combinada alternada:", combinada)