b = []
x=1
for x in range(5):
        c = int(input("Podaj liczbę "))
        if(c>-11 and c<11):
            b.append(c)
        else:
            continue
print(b)

