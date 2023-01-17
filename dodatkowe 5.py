import random
iloczyn = 1
for i in range(10):
    a = random.randint(1, 10)
    if a % 2 == 1:
        iloczyn *= a
        print(a)
print(f"Iloczyn: {iloczyn}")