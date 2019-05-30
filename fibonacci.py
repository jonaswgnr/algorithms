def fibonacci(x):
    if x in tmp:
        return tmp[x]
    else:
        tmp[x] = fibonacci(x-2) + fibonacci(x-1)
        return tmp[x]

tmp = {0:0, 1:1}
fibonacci(int(input("Zahl: ")))
for value in tmp.values():
    print(value)
