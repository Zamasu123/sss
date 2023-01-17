def zad2_2(L, a , b):
    L2 = []
    for x in L:
        if a <= x <= b:
            L2.append(x)
    return L2


n = int(input("Podaj liczbę: "))
ile = 0
L = []
for i in range(n):
    a = int(input(f"Podaj liczbę {i+1}: "))
    L.append(a)
print(L)
wynik = zad2_2(L, 0, 10)
print(wynik)