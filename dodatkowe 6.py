import random
def zad4(n, x, y):
    L = []
    for i in range(n):
        a = random.randint(x, y)
        L.append(a)
    return L



def zad6(L):
    L2 = []
    for x in L:
        if x >= 0:
            L2.append(True)
        else:
            L2.append(False)
    return L2

W = zad4(10, -10, 10)
print(W)
B = zad6(W)

licznik_False = 0
licznik_True = 0
for i in range(len(B)):
    if B[i] == True:
        licznik_True += 1
    else:
        licznik_False += 1
print(f"True: {licznik_True}, False = {licznik_False}")

L2 = []
for x in W:
    if x >= 0:
        L2.append(True)
    else:
        L2.append(False)
print(L2)