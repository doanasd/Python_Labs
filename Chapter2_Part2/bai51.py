def is_good_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return len(password) >= 8 and has_upper and has_lower and has_digit

password = input("Nhập mật khẩu: ")
if is_good_password(password):
    print("Mật khẩu của bạn là tốt.")
else:
    print("Mật khẩu của bạn không tốt. Nó phải dài ít nhất 8 ký tự và chứa ít nhất một chữ hoa, một chữ thường, và một số.")
Bài 52: Kiểm tra số hoàn hảo và tìm số hoàn hảo

Python
