unit_val = int(input("Enter units: "))

if unit_val <= 100:
    total = unit_val * 6
elif unit_val <= 200:
    total = unit_val * 8
else:
    total = unit_val * 12

print("Total bill amount:", total)