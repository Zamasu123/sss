import numpy as np

tab = [2 ** i for i in range(7,-1,-1)]
print(tab)

wagi = np.array(tab)
print(wagi)

liczba_bin = np.random.randint(low=0, high=2, size=(8))
print(liczba_bin)

liczba_dzies = liczba_bin * wagi
print(liczba_dzies.sum())