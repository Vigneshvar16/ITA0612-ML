balance = 5000
pin = 1234

user_pin = int(input("Enter PIN: "))

if user_pin == pin:
    amount = float(input("Enter Withdrawal Amount: "))

    if amount <= balance:
        balance -= amount
        print("Transaction Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")