thang = input("Nhập tên tháng: ").lower()

if thang in ["tháng 1", "tháng 3", "tháng 5", "tháng 7", "tháng 8", "tháng 10", "tháng 12"]:
    print("Tháng có 31 ngày.")
elif thang in ["tháng 4", "tháng 6", "tháng 9", "tháng 11"]:
    print("Tháng có 30 ngày.")
elif thang == "tháng 2":
    print("Tháng có 28 hoặc 29 ngày.")
else:
    print("Tên tháng không hợp lệ.")
