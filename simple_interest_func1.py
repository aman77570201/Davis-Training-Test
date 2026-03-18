def find_si(pr, rt, tm):
    si = (pr * rt * tm) / 100
    print("Simple Interest =", si)

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

find_si(p, r, t)