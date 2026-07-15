basic = float(input("Enter Basic Salary: "))

pf = basic * 0.12
tax = basic * 0.10

gross = basic
net = gross - pf - tax

print("Gross Salary:", gross)
print("PF:", pf)
print("Tax:", tax)
print("Net Salary:", net)