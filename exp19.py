stock = int(input("Current Stock: "))
minimum = int(input("Minimum Stock: "))

if stock < minimum:
    print("Restock Required")
else:
    print("Stock Available")