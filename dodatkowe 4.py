import random
def zad4(n, x, y):
    L = []
    for i in range(n):
        a = random.randint(x, y)
        L.append(a)
    return L

W = zad4(5, 10, 20)
print(W)
W = zad4(24, 20, 100)
print(W)