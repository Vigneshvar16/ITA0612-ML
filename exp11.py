distance = float(input("Distance (km): "))
mileage = float(input("Mileage (km/l): "))
price = float(input("Fuel Price/litre: "))

litres = distance / mileage
cost = litres * price

print("Fuel Cost:", cost)