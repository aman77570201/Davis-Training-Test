def compute_si(p, r, t):
    si = (p * r * t) / 100
    return si

principal = float(input("Enter P: "))
rate = float(input("Enter R: "))
time = float(input("Enter T: "))

print("Simple Interest:", compute_si(principal, rate, time))