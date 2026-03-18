def si_formula(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

print("Simple Interest:", si_formula(p, r, t))