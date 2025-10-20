# Bài 1: Xử lý ngoại lệ FileNotFoundError

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"File {filename} không tồn tại."
    print(msg)
