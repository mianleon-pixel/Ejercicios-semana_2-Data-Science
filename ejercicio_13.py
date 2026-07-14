nombres = ['Ana', 'Luis', 'Ana', 'Carlos', 'Luis', 'Ana', 'Maria', 'Carlos']
nombres_unicos = set(nombres)
for nombre in nombres_unicos:   
    apariciones = nombres.count(nombre)
    print(f"El nombre {nombre} aparece {apariciones} veces.")