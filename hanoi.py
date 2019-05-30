def hanoi (q,z,p,n):
  if n is 1:
    print("Bewege ", q," zu", z)
    return 0
  hanoi(q,p,z,n-1)
  hanoi(q,z,p,1)
  hanoi(p,z,q,n-1)

q="quelle"
z="ziel"
p="puffer"
n= int(input("Anzahl Scheiben: "))
hanoi(q,z,p,n)