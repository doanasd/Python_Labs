# Part3 - Bài 2: Đếm số từ trong file với xử lý ngoại lệ
filename = input("Enter filename to count words (default alice.txt): ") or "alice.txt"
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found:", filename)
else:
    words = contents.split()
    print(f"File {filename} có {len(words)} từ")
