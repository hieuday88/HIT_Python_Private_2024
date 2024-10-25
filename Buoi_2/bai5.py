
a = int(input("Nhap a: "))

bit_count = len(oct(a)[2:]) * 3
print(f"So luong bit can thiet: {bit_count}")

print("Danh sach thuoc tinh va phuong thuc cua so a:")
print(dir(a))
