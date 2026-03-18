def calculate_si(p, r, t):
    return (p * r * t) / 100

P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

si = calculate_si(P, R, T)

print("Simple Interest:", si)