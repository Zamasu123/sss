Wiek = input ('podaj wiek')
Wiek = int(Wiek)
if Wiek < 4:
    Cena = 0
elif Wiek <= 18:
    Cena = 10
else: Cena = 20

print(f'Cena biletu {Cena} zł')
