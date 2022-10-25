
#Zadanie 2
x=input("Podaj literę:")
if len(x)>1 or lex(x)==0:
    print("Błąd")
    exit()
if 'a'<=x <='z':
    print("litera jest mała")
elif 'A'<=x <="Z":
    print("litera jest duża")
else:
    print("Podana wartość nie jest literą")