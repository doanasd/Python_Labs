# Bài 17: Tính chỉ số gió lạnh (Wind Chill Index)
import math
Ta = float(input("Nhiệt độ (°C): "))
V = float(input("Tốc độ gió (km/h): "))
WCI = 13.12 + 0.6215*Ta - 11.37*(V**0.16) + 0.3965*Ta*(V**0.16)
print("Wind Chill Index (làm tròn):", round(WCI))
