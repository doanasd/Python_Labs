numbers = []
while True:
    try:
        n = int(input("Nhập một số nguyên (0 để kết thúc): "))
        if n == 0:
            break
        numbers.append(n)
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")

numbers.sort()
for num in numbers:
    print(num)
Bài 37: Loại bỏ từ trùng lặp và giữ nguyên thứ tự

Python
