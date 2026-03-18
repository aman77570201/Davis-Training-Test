units_used = int(input("Enter units: "))

if units_used <= 100:
    total_bill = units_used * 7
elif units_used <= 200:
    total_bill = units_used * 9
else:
    total_bill = units_used * 15

print("Total bill amount:", total_bill)