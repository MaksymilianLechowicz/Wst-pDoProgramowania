#zadanie 1

a=int(input("Proszę podać a "))
b=int(input("Proszę podać b "))
if(a>b):
    c=b
    d=a
else:
    c=a
    d=b
while(c<=d):
    print(c, end=" ")
    c+=1


#a=int(input("Proszę podać a "))
#b=int(input("Proszę podać b "))
#if a > b:
#    a, b = b, a
#while a <= b:
#    print(a, end=" ")
#    a += 1