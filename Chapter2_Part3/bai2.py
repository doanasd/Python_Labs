# Bài 2: Xử lý ngoại lệ FileNotFoundError khi đếm số từ trong file

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"File {filename} không tồn tại."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print(f"File {filename} có {num_words} từ.")
