values=[10,20,33]
keys=['dziesięć','dwadzieścia','trzydzieści']
D={}
print(list(zip(keys,values)))
D=dict(zip(keys,values))
for i in range (len(values)):
    D[keys[i]]=values[i]

print(D)
A=dict(trzydzieści=30, czterdzieści=40, pięćdziesiąt=50)
print(A)
# D.update(A)
D3=D.copy()
D3.update(A)
print(D3)