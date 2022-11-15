zwierzeta = []
f = int(input("Podaj liczbę zwierząt które chcesz dodać "))
i = 0
for i in range(0, f):
    b = input("podaj nazwe zwierzecia ")
    zwierzeta.append(b)
a= sorted(zwierzeta)
print(a)
print(zwierzeta[0])
print(zwierzeta[-3])
print(zwierzeta[-2])
print(zwierzeta[-1])
print(len(zwierzeta))