palabras = ['python', 'sol', 'programacion', 'lista', 'computadora', 'if', 'variable']
contador_largas = 0
for palabra in palabras:
       if len(palabra) > 5:
              contador_largas = contador_largas + 1 
print("La cantidad de palabras con más de 5 letras es:", contador_largas)