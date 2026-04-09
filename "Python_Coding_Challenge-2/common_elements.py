list1 = [1,2,3]
list2 = [2,3,4]

result = []
for i in list1:
    if i in list2:
        result.append(i)

print(result)