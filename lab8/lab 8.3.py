def potega(a, b):
    c = []
    if len(a) != len(b):
        return()
    else:
        for i in range(len(a)):
            c.append(a[i] ** b[i])
        return c
a = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]
b = [2 ,2 ,1 ,3 ,2 ,2 ,1 ,2 ]

print(potega(a,b))

