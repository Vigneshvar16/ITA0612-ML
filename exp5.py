amount = float(input("Purchase Amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

subtotal = amount - discount
gst = subtotal * 0.18
total = subtotal + gst

print("Final Bill:", total)