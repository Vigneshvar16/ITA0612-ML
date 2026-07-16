vehicle = input("Vehicle (bike/car): ")
hours = int(input("Hours: "))

if vehicle.lower() == "bike":
    fee = hours * 20
else:
    fee = hours * 50

print("Parking Fee:", fee)