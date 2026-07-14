textos = ['hola', '', 'python', '', 'listas', '', 'programar', '']
textos_limpios = []
for t in textos:
        if t != '':
              textos_limpios.append(t)
print("Lista sin vacíos:", textos_limpios)