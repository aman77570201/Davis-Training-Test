unit_input = int(input("Enter units: "))

if unit_input <= 100:
    cost = unit_input * 6
elif unit_input <= 200:
    cost = unit_input * 10
else:
    cost = unit_input * 14

print("Total bill amount:", cost)