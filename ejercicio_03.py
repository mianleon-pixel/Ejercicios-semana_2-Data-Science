numeros = [45, 12, 89, 34, 89, 23, 67, 10]
numeros_unicos = list(set(numeros))
numeros_ordenados = sorted(numeros_unicos)
segundo_mayor = numeros_ordenados[-2]
print("Lista ordenada sin repetidos:", numeros_ordenados)
print("El segundo número mayor es:", segundo_mayor)