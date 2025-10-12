import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
A = float(input("Enter angle A (radian): "))
B = float(input("Enter angle B (radian): "))
C = float(input("Enter angle C (radian): "))
s = (a + b + c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Triangle area:", area)
