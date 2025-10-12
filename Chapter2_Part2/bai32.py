def caesar_cipher(message, shift, mode):
    result = ""
    for char in message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if mode == 'encode':
                new_char_code = (ord(char) - start + shift) % 26 + start
            elif mode == 'decode':
                new_char_code = (ord(char) - start - shift + 26) % 26 + start
            result += chr(new_char_code)
        else:
            result += char
    return result

mode = input("Nhập 'encode' để mã hóa hoặc 'decode' để giải mã: ")
message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số ký tự dịch chuyển: "))

if mode == 'encode':
    print("Tin nhắn đã mã hóa:", caesar_cipher(message, shift, 'encode'))
elif mode == 'decode':
    print("Tin nhắn đã giải mã:", caesar_cipher(message, shift, 'decode'))
else:
    print("Chế độ không hợp lệ.")
Bài 33: Kiểm tra Palindrom

Python
