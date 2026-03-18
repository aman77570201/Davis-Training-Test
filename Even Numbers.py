def even_list(n):
    evens = []
    for i in range(1, n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens

N = int(input("Enter N: "))
print(even_list(N))