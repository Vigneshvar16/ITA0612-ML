food = float(input("Food Amount: "))

gst = food * 0.05
service = food * 0.10

total = food + gst + service

print("Restaurant Bill:", total)