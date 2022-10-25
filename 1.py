#Zadanie 1
x=int(input("Wiek klienta:"))
y=0
if  x<4:
    print("Koszt biletu wynosi:", y, "zł")
elif x<18:
        y=+10
        print("Koszt biletu wynosi:", y, "zł")
else:
    y=+20
    print("Koszt biletu wynosi:", y, "zł")

