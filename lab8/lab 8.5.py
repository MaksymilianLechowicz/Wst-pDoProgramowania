def dodawanie(a,b):
    return a+b
def odejmowanie(a,b):
    return a-b
def mnożenie(a,b):
    return a*b
def dzielenie(a,b):
    if b == 0:
        return
    else:
        return a/b

Kalkulator = {"+": dodawanie, "-":odejmowanie, "*":mnożenie, "/":dzielenie}
u1 = float(input("Proszę podać liczbę a "))
u2 = float(input("Proszę podać liczbę b "))

działanie = input('Podaj działanie ')

print(Kalkulator[działanie](u1,u2))
