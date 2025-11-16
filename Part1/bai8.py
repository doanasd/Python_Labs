# Bài 8: Diện tích tam giác đều theo Heron
import math
a = float(input("Nhập cạnh tam giác đều: "))
s = (a*3)/2
area = math.sqrt(max(0, s*(s-a)*(s-a)*(s-a)))
print("Diện tích tam giác đều:", area)
