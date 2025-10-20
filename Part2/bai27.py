so_canh = int(input("Nhập số cạnh (3-10): "))

if so_canh == 3:
    print("Hình tam giác")
elif so_canh == 4:
    print("Hình tứ giác")
elif so_canh == 5:
    print("Hình ngũ giác")
elif so_canh == 6:
    print("Hình lục giác")
elif so_canh == 7:
    print("Hình thất giác")
elif so_canh == 8:
    print("Hình bát giác")
elif so_canh == 9:
    print("Hình cửu giác")
elif so_canh == 10:
    print("Hình thập giác")
else:
    print("Số cạnh không hợp lệ, chương trình chỉ hỗ trợ từ 3 đến 10 cạnh.")
