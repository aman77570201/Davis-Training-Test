lst = [10,20,5,15]

first = second = -9999

for i in lst:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print(second)