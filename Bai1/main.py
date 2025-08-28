import math

# Nhập hệ số a, b, c
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Tính delta
delta = b**2 - 4*a*c

if a == 0:
    print("Đây không phải là phương trình bậc 2.")
elif delta < 0:
    print("Phương trình vô nghiệm.")
elif delta == 0:
    x = -b / (2*a)
    print(f"Phương trình có nghiệm kép: x = {x}")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")