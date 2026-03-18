units_val = int(input("Enter units consumed: "))

if units_val <= 100:
    bill_amt = units_val * 5
elif units_val <= 200:
    bill_amt = units_val * 9
else:
    bill_amt = units_val * 13

print("Total bill amount:", bill_amt)