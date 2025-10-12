sec = int(input("Enter number of seconds: "))
days = sec // 86400
sec %= 86400
hours = sec // 3600
sec %= 3600
minutes = sec // 60
sec %= 60
print("Days:", days, "Hours:", hours, "Minutes:", minutes, "Seconds:", sec)
