import random

zestaw_1 = []

x = int(input("Podaj liczbę elementów listy: "))

for z in range(x):
    y = random.randint(1, 10)
    zestaw_1.append(y)
print(zestaw_1)

a = int(input("Podaj liczbę elementów listy: "))

zestaw_2 = [random.randint(5, 15) for z in range(x)]
print(zestaw_2)

c = int(input("Podaj liczbę: "))

if c in zestaw_1:
    print("Liczba z listy 1")
elif c in zestaw_2:
    print("Liczba z listy 2")
else:
    print("Nie ma takiej liczby w obu zestawach")

suma_zestawów = zestaw_1 + zestaw_2
print(suma_zestawów)

suma_zestawów.sort()
print(suma_zestawów)