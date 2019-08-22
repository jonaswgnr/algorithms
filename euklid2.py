
a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))
rest = a%b

while rest != 0:
    rest = a%b
    a=b
    b=rest
    print(a, " / ", b, "Rest: ",rest)
print("GGT ist: ",a)