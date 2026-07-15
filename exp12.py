amount = float(input("Recharge Amount: "))

if amount >= 500:
    cashback = 50
elif amount >= 300:
    cashback = 20
else:
    cashback = 0

final = amount - cashback

print("Final Recharge:", final)