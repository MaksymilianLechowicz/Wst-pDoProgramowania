#zad 2
import random
x= int(input("Podaj długość listy "))
L1 = []
for i in range (x):
    L1.append(random.randrange(1,11))
    x-=1
print(L1)