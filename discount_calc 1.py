item_price = float(input("Enter price: "))
disc_percent = float(input("Enter discount percentage: "))

deduction = item_price * disc_percent / 100
final_cost = item_price - deduction

print("Final price after discount =", final_cost)