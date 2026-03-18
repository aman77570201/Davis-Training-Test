base_price = float(input("Enter price: "))
disc_rate = float(input("Enter discount %: "))

discount_amt = (base_price * disc_rate) / 100
total_pay = base_price - discount_amt

print("Final price after discount:", total_pay)