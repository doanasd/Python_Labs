def ma_hoa_caesar(message):
    encrypted_message = ""
    for char in message:
        if 'a' <= char <= 'z':
            encrypted_message += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_message += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message

message = input("Nhập tin nhắn cần mã hóa: ")
print("Tin nhắn đã mã hóa:", ma_hoa_caesar(message))
Bài 32: Mã hóa/Giải mã Caesar với số dịch chuyển tùy chỉnh

Python
