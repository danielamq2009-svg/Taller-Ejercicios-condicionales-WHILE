A = int(input("Ingrese el entero A: "))
B = int(input("Ingrese el entero B: "))
entero = A + 1
while A < B and A < entero < B:
    print(entero)
    entero += 1
while A+1 == B:
    print("No hay enteros interiores.")
    break
