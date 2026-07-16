age = int(input("Age: "))
nationality = input("Nationality: ")

if age >= 18 and nationality.lower() == "indian":
    print("Eligible")
else:
    print("Not Eligible")