notas = [14, 18, 11, 16, 9, 13, 20]
suma_notas = sum(notas)
cantidad_notas = len(notas)
promedio = suma_notas / cantidad_notas
print("El promedio del estudiante es:", round(promedio, 2))
if promedio >= 11:
    print("Estado: APROBADO")
else:
    print("Estado: DESAPROBADO")