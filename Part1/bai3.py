# Bài 3: Trích host từ chuỗi chứa email và các thông tin khác
data = input("Enter the string containing email: ").strip()
start = data.find('@')
if start == -1:
    print("Không tìm thấy @")
else:
    end = data.find(' ', start)
    if end == -1:
        host = data[start+1:]
    else:
        host = data[start+1:end]
    print("Host:", host)
