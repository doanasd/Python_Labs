# Bài 12: Tính thuế và tiền boa
meal = float(input("Chi phí bữa ăn: "))
tip = 0.18 * meal
tax = 0.05 * meal
total = meal + tip + tax
print(f"Thuế: {tax:.2f}, Tiền boa: {tip:.2f}, Tổng: {total:.2f}")
