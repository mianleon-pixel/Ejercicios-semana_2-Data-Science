lista1 = [1, 3, 5, 7, 9, 11]
lista2 = [2, 3, 6, 7, 10, 11]
comunes = []
for n in lista1:   
    if n in lista2:        
        comunes.append(n)
print("Elementos comunes en ambas listas:", comunes)