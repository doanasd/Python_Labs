# Bài 5: In 5 ký tự đầu, 5 ký tự cuối, 4 chuỗi trên một dòng, 4 chuỗi trên 4 dòng
s = input("Enter your string: ")
first5 = s[:5]
last5 = s[-5:] if len(s)>=5 else s
print("First five characters:", first5)
print("Last five characters:", last5)
print("Four strings in one line:", (s + " ")*4)
print("Four strings in four lines:\n" + "\n".join([s]*4))
