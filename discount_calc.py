cost = float(input("Enter product price: "))
disc = float(input("Enter discount %: "))

discount_value = (cost * disc) / 100
amount_payable = cost - discount_value

print("Final Amount =", amount_payable)