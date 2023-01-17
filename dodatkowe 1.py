def suma(n):
    suma = 0
    for i in range(n):
        a = float(input(f"Podaj liczbę {i + 1}: "))
        suma += a
    return suma

n = int(input("Podaj liczbę: "))
wynik = suma(n)
print(f"Suma {n} liczb: {wynik}")