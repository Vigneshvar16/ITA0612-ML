attended = int(input("Classes Attended: "))
total = int(input("Total Classes: "))

percentage = (attended / total) * 100

print("Attendance:", percentage)

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")