# Bài 2: Trích host từ email
data = input("Enter email (e.g. name@gmail.com): ").strip()
pos = data.find('@')
if pos != -1:
    host = data[pos+1:]
    print("Host:", host)
else:
    print("Không tìm thấy ký tự @")
