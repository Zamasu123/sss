import numpy as np

tablica = np.random.randint(low=0, high=50, size=(5, 5))
print(tablica)

print(f" max: {tablica.max()}")
print(f" min: {tablica.min()}")

print(f" max in row: {tablica.max(axis=1)}")
print(f" max in column: {tablica.max(axis=0)}")

print(f" suma in row: {tablica.sum(axis=1)}")
print(f" suma in column: {tablica.sum(axis=0)}")