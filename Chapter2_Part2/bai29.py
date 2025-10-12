a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))

if a == b == c:
    print("Đây là tam giác đều.")
elif a == b or a == c or b == c:
    print("Đây là tam giác cân.")
else:
    print("Đây là tam giác thường.")
Bài 30: Kiểm tra năm nhuận

Python
