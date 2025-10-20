# Bài 3: Đếm số từ trong nhiều file

def count_words(filename):
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

filenames = ['f1.txt', 'f2.txt', 'f3.txt']

for filename in filenames:
    count_words(filename)
