n = int(input("Enter N: "))

evens = []
for i in range(1, n + 1):
    if i % 2 == 0:
        evens.append(i)

print("Even numbers list:", evens)