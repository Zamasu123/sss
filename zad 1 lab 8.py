def find(lista,liczba):
    lista2=[]
    index = 0
    for i in lista:
        if liczba == i:
            lista2.append(index)
        index += 1
    return lista2

L1 = find([3,4,2,1,5,2,3,7],2)
print(L1)