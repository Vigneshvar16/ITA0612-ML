seats = int(input("Number of Seats: "))
category = input("Category (silver/gold): ")

if category.lower() == "gold":
    price = 250
else:
    price = 150

total = seats * price

if seats >= 5:
    total *= 0.9

print("Ticket Cost:", total)