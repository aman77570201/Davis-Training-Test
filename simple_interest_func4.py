def simple_int(p, r, t):
    return (p * r * t) / 100

P = float(input("Enter P: "))
R = float(input("Enter R: "))
T = float(input("Enter T: "))

si_result = simple_int(P, R, T)

print("Simple Interest:", si_result)