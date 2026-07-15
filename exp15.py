temps = []

for i in range(7):
    t = float(input(f"Day {i+1}: "))
    temps.append(t)

print("Maximum:", max(temps))
print("Minimum:", min(temps))
print("Average:", sum(temps) / 7)