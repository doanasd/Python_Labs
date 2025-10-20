# Bài 7: Diện tích tam giác theo Heron
import math
a = float(input("a (cạnh): "))
b = float(input("b (cạnh): "))
c = float(input("c (cạnh): "))
s = (a+b+c)/2
area = math.sqrt(max(0, s*(s-a)*(s-b)*(s-c)))
print("Diện tích tam giác (Heron):", area)
