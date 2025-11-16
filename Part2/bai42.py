def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Nhập một số để tính giai thừa: "))
result = factorial(number)
print(str(result))
