char = input("Nhập một chữ cái: ").lower()

if char in ['a', 'e', 'i', 'o', 'u']:
    print("Đây là một nguyên âm.")
elif char == 'y':
    print("Y có thể là nguyên âm hoặc phụ âm.")
else:
    print("Đây là một phụ âm.")
Bài 27: Xác định tên hình dạng

Python
