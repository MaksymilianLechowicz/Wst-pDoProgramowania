def find(l1,int):
    l2 = []
    for i in range(len(l1)):
        if l1[i] == int:
            l2.append(i)
        return(l2)
        print(l2)
find([1,2,3,4],3)