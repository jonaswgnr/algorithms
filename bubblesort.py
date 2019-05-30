def bubblesort(numbers):
    for i in range(len(numbers) - 1):
        for x in range(len(numbers) - 1):
            if numbers[x] > numbers[x + 1]:
                tmp = numbers[x + 1]
                numbers[x + 1] = numbers[x]
                numbers[x] = tmp
    return numbers


numbers=list(input("Zu sortierende Zahlen eingeben: "))
print("Sortierte Zahlen: ", bubblesort(numbers))