# Q1.A shopkeeper wants to calculate total bill after discount
# Input price and discount percentage
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

# Calculate discount amount
discount_amount = (price * discount) / 100

# Calculate final price
final_price = price - discount_amount

# Output final price
print("Final price after discount =", final_price)