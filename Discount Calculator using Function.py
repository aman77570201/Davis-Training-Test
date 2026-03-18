def discount_price(price, discount):
    final_price = price - (price * discount / 100)
    return final_price

price = float(input("Enter Price: "))
discount = float(input("Enter Discount %: "))

result = discount_price(price, discount)

print("Final price after discount =", result)