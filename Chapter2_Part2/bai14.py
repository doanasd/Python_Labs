values = []
for i in range(100, 301):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        values.append(s)
print(",".join(values))
Bài 15: Chuyển chuỗi số thành danh sách và tuple

Python
