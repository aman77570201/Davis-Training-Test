price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

final_amount = price * (100 - discount) / 100

print("Final price after discount:", final_amount)