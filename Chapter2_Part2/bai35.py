numbers_str = input("Nhập các số, phân tách bằng dấu phẩy: ")
numbers = [int(num) for num in numbers_str.split(',')]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)
