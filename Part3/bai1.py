# Part3 - Bài 1: Ví dụ xử lý FileNotFoundError
filename = 'alice.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"File {filename} không tồn tại.")
else:
    print(f"Đọc file {filename} thành công, độ dài:", len(contents))
