limit_input = int(input("Enter N: "))

even_nums = [num for num in range(1, limit_input + 1) if num % 2 == 0]

print("Even numbers list:", even_nums)
