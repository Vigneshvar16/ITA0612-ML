age = int(input("Age: "))
weight = float(input("Weight: "))
hb = float(input("Hemoglobin: "))

if age >= 18 and weight >= 50 and hb >= 12.5:
    print("Eligible")
else:
    print("Not Eligible")