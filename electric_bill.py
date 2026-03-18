units_used = int(input("Enter electricity units: "))

if units_used <= 100:
    bill = units_used * 5
elif units_used <= 200:
    bill = units_used * 7
else:
    bill = units_used * 10

print("Total Bill =", bill)