
salario = float(input("Salario mensual: "))
if salario > 0:
    while salario > 0:
        dias = int(input("Dias trabajados: "))
        bonos = float(input("Bonos: "))
        deducciones = float(input("Otras deducciones: "))
        if 0 <= dias <= 30 and bonos >= 0 and deducciones > 0:

            proporcional = salario * dias / 30
            devengado = proporcional + bonos
            neto = devengado * 0.83 - deducciones

        print("Pago neto:", neto)
        break
else:
        print("Sin trabajadores")
