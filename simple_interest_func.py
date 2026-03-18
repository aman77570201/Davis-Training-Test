def calc_si(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

result = calc_si(p, r, t)

print("Simple Interest =", result)