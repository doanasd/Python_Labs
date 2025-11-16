# Bài 11: Diện tích cánh đồng đổi sang mẫu Anh
width = float(input("Chiều rộng (m): "))
length = float(input("Chiều dài (m): "))
sqm = width * length
acre = sqm / 43560.0
print(f"Diện tích: {acre:.6f} mẫu Anh")
