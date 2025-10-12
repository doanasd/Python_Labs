text = input("Nhập một chuỗi: ")
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Chuỗi '" + text + "' là một Palindrom.")
else:
    print("Chuỗi '" + text + "' không phải là một Palindrom.")
Bài 34: Chuyển đổi số thập phân sang nhị phân

Python
