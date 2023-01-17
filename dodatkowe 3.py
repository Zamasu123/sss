n = int(input("Podaj liczbę: "))
L = []
for i in range(n):
    a = int(input(f"Podaj liczbę {i + 1}: "))
    if a % 3 == 0:
        L.append(a)
print(L)