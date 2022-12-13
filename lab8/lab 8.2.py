def sum_of_values(bo):
    n = 0
    for i in bo.values():
        n += i
    return(n)
bo = { '1' : 10,
       '2' : -4,
       '3' : 3
       }
print(sum_of_values(bo))