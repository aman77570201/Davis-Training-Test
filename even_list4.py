limit_val = int(input("Enter N: "))

even_list = []
for x in range(2, limit_val + 1, 2):
    even_list.append(x)

print("Even numbers list:", even_list)