numeros = [12, 7, 9, 24, 31, 18, 5, 42, 13, 8]
pares = []
impares = []
for n in numeros:  
    if n % 2 == 0:
        pares.append(n)  
    else:
        impares.append(n)
print("Números pares:", pares)
print("Números impares:", impares)