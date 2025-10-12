Ta = float(input("Enter temperature (Celsius): "))
V = float(input("Enter wind speed (km/h): "))
WCI = 13.12 + 0.6215*Ta - 11.37*(V**0.16) + 0.3965*Ta*(V**0.16)
print("Wind chill index:", round(WCI))
