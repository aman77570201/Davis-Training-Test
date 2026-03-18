def si_calc(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

print("Simple Interest:", si_calc(p, r, t))