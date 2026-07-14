frutas = ['manzana', 'pera', 'uva', 'sandía', 'plátano', 'mango']
busqueda = input("Escribe el nombre de una fruta: ").lower().strip()
if busqueda in frutas:
    posicion = frutas.index(busqueda)
    print(f"La fruta '{busqueda}' está en la posición {posicion}.")
else:
    print(f"La fruta '{busqueda}' no se encuentra en la lista.")