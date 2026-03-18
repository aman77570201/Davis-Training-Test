consumed_units = int(input("Enter units: "))

if consumed_units <= 100:
    total = consumed_units * 4
elif consumed_units <= 200:
    total = consumed_units * 6
else:
    total = consumed_units * 9

print("Total bill amount =", total)