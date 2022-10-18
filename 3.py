# Przykład: Jaką operację chcesz wykonać?
# 1) dodawanie
# 2) odejmowanie
# 3) mnożenie
# 4) dzielenie
# 5) potęgowanie
# Wpisz numer operacji: 2
# Podaj argument 1: 34
# Podaj argument 2: 5
# Wynik: 29

print('''
1)dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
''')
x = int(input('what operation do you want to perform?1'))
a = int(input('podaj a:'))
b = int(input('podaj b:'))
if x == 1:
    print(a+b)
elif x == 2:
    print(a-b)
elif x == 3:
    print(a*b)
elif x == 4:
    print(a/b)
elif x == 5:
    print(a**b)
else:
    print('not a valid number')