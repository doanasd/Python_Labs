import random

def generate_password():
    length = random.randint(7, 10)
    password = ""
    for _ in range(length):
        password += chr(random.randint(33, 126))
    return password

print("Mật khẩu ngẫu nhiên của bạn là:", generate_password())
Bài 51: Kiểm tra mật khẩu tốt

Python
