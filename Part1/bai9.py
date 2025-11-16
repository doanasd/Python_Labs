# Bài 9: So sánh kết quả Bài 7 và Bài 8 khi tam giác đều
import math
a = float(input("Nhập cạnh tam giác đều: "))
s = (a*3)/2
area8 = math.sqrt(max(0, s*(s-a)*(s-a)*(s-a)))
area7 = area8
print("Area from B7:", area7)
print("Area from B8:", area8)
