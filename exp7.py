p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

si = (p * r * t) / 100
ci = p * ((1 + r / 100) ** t) - p

print("Simple Interest:", si)
print("Compound Interest:", ci)