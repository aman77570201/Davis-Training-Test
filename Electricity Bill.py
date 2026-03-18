def light_bill(units):
    total = 0
    
    if units > 200:
        total += (units - 200) * 10
        units = 200
        
    if units > 100:
        total += (units - 100) * 7
        units = 100
        
    total += units * 5
    
    return total

u = int(input("Enter Units: "))
print("Total Bill =", light_bill(u))