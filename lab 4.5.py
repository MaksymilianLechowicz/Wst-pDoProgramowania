import random

#punkty = []
#for i in range (0,15):
#    a = round(random.uniform(0, 50), 2)
#    punkty.append(a)

punkty = [round(random.uniform(0, 50), 2) for i in range(15)]
print(punkty)
print(max(punkty), min(punkty))
print("Średnia wynosi: ",sum(punkty)/len(punkty))
g = float(input("Prosze podać licbę punktów: "))
if  g in punkty:
    print(punkty.index(g))
else:
    print("Brak wartości w liście")
o = sum(punkty)/len(punkty)
h=0
for k in range(15):
    if(punkty[k]<o):
        h+=1
print(h)
j=0
for k in range(15):
    if(punkty[k]>o):
        j+=1
print(j)
