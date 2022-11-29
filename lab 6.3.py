
def job(*na):
    for i in na:
        print(i)

job(1,60)

job(8,300,19)

def job(*na):
    for i in na:
        print(i)
def max(num1,*args):
    m = num1
    for i in args:
        if m < i:
            m = 1
    return m
print(max(8,-4,5,7))