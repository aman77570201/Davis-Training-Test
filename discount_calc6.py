price_input = float(input("Enter price: "))
discount_input = float(input("Enter discount %: "))

final_price = price_input * (1 - discount_input / 100)

print("Final price after discount:", final_price)