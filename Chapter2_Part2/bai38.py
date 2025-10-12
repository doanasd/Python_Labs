neg_nums = []
zero_nums = []
pos_nums = []

while True:
    inp = input("Nhập một số nguyên (dòng trống để kết thúc): ")
    if not inp:
        break
    num = int(inp)
    if num < 0:
        neg_nums.append(num)
    elif num == 0:
        zero_nums.append(num)
    else:
        pos_nums.append(num)

sorted_list = neg_nums + zero_nums + pos_nums
for num in sorted_list:
    print(num)
Bài 39: Tạo từ điển (i, i*i)

Python
