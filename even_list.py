limit = int(input("Enter N: "))

print("Even Numbers:")
for num in range(1, limit + 1):
    if num % 2 == 0:
        print(num, end=" ")