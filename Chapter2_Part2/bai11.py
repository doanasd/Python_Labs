numlist = list()
while (True):
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("Giá trị Trung bình:", average)
print(numlist)
Bài 12: Tìm số chia hết cho 7 nhưng không chia hết cho 5

Python
