def simple_interest(P, R, T):
    return (P * R * T) / 100

P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

print("Simple Interest =", simple_interest(P, R, T))