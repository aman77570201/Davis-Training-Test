def even_numbers(N):
    for i in range(2, N+1, 2):
        print(i, end=" ")

N = int(input("Enter N: "))
even_numbers(N)