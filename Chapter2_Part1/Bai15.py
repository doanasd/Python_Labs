import math
t = float(input("Enter temperature in Celsius: "))
v = float(input("Enter speed in m/s: "))
wci = 13.12 + 0.6215*t - 11.37*(v**0.16) + 0.3965*t*(v**0.16)
print("Wind chill index:", round(wci))
