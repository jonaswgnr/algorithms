def hanoi (q,z,p,n):
  if n is 1:
    print("Move ", q," to", z)
    return 0
  hanoi(q,p,z,n-1)
  hanoi(q,z,p,1)
  hanoi(p,z,q,n-1)

q="quelle"
z="ziel"
p="puffer"
n=5
#hanoi(q,z,p,n)