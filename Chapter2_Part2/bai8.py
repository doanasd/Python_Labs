import string

my_str = "Hello!!!, he said ---and went."
st2 = ""
for char in my_str:
    if char.isalnum() or char.isspace():
        st2 += char
print(st2)
Bài 9: Sắp xếp từ theo thứ tự bảng chữ cái

Python
