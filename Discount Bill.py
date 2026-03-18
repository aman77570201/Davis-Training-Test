def bill_after_discount(price, discount):
    discount_amount = (price * discount) / 100
    final = price - discount_amount
    return final

p = float(input("Enter Price: "))
d = float(input("Enter Discount %: "))

print("Final Price =", bill_after_discount(p, d))