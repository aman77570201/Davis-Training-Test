amt = float(input("Enter price: "))
disc = float(input("Enter discount %: "))

payable = amt - (amt * disc / 100)

print("Final price after discount:", payable)