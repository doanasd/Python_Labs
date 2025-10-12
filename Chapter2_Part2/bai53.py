def get_sublists(my_list):
    sublists = [[]]
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            sublists.append(my_list[i:j+1])
    return sublists

my_list = [1, 2, 3]
print("Các danh sách con của", my_list, "là:", get_sublists(my_list))
Bài 54: Định dạng danh sách từ tiếng Anh

Python
