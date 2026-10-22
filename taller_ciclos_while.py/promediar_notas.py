promedio = 0
suma = 0
cantidad = 0

nota = int(input("Ingrese la nota: "))
if nota != -99:
    while 0 <= nota <= 100:
        suma = suma + nota
        nota = int(input("Ingrese la nota: "))
        cantidad += 1
        if nota == -99:
            break
    print("Cantidad: ", cantidad)
    print("Promedio: ", suma/cantidad)
else: 
    print("Cantidad", cantidad)
    print("Sin notas")
