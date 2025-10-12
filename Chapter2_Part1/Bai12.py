meal = float(input("Enter meal cost: "))
tip = meal * 0.18
tax = meal * 0.05
total = meal + tip + tax
print("Meal:", f"{meal:.2f}")
print("Tip:", f"{tip:.2f}")
print("Tax:", f"{tax:.2f}")
print("Total:", f"{total:.2f}")
