estudiantes = ['Ana', 'Luis', 'Carlos', 'María', 'Pedro']
notas = [18, 10, 14, 8, 16]
aprobados = []
for estudiante, nota in zip(estudiantes, notas):
    if nota >= 11:
        aprobados.append(estudiante)
print("Estudiantes aprobados:", aprobados)