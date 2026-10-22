c = 0
i = 0
m = 0

while True:
    c = float(input("Capital: "))
    i = float(input("Tasa: "))
    m = int(input("Años: "))

    if c >= 0 and 0 < i < 100 and m > 0:
        break

for k in range(1, m + 1):
    c = c * (1 + i / 100)
    print("Saldo año", k, ":", c)

print("Saldo final:", c)