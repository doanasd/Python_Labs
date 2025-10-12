def giaithua(x):
    if x == 0:
        return 1
    return x * giaithua(x - 1)

x = int(input("Nhập số cần tính giai thừa:"))
print("Giai thừa của", x, "là:", giaithua(x))
Bài 21: Tạo và in danh sách bình phương từ 1 đến 20

Python
