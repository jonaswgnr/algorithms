def newtonroot(checknum):
    checknum = (checknum + (x / checknum)) / 2
    return checknum

x = float(input("Berechne Wurzel von: "))
checknum = float(input("Startwert: "))
iterations = int(input("Anzahl Iterationen: "))

for i in range(iterations):
    checknum = newtonroot(checknum)
    print("Zwischenergebnis: ",checknum)