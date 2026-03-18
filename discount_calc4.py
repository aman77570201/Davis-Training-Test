price_val = float(input("Enter price: "))
disc_val = float(input("Enter discount %: "))

final_bill = price_val - (price_val * disc_val / 100)

print("Final price after discount:", final_bill)