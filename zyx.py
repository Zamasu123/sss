litera = input ('podaj litere')
if (len(litera)>1):
    print("Wprowadzono wiecej niż 1 literę")
    exit()
if (len(litera)==0):
    print("Nie wprowadzono Litery")
    exit()

if ('a'<= litera <='z'):
    print("Mała litera")
elif ('A'<= litera <='Z'):
    print("Duża litera")
else:
    print("Nie jest literą")
