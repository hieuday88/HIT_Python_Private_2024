print("Nhap so phan tu cua tuple A: ")
n = int(input())
print("Nhap cac phan tu tuple A (so nguyen): ")
a = tuple(int(input()) for _ in range(n))

print("Nhap so phan tu cua tuple B: ")
m = int(input())
print("Nhap cac phan tu tuple B (chuoi ky tu): ")
b = tuple(input() for _ in range(m))

tbc = sum(a) / len(a)
count = sum(1 for i in a if i > tbc)
print(f"So luong phan tu trong A lon hon trung binh cong ({tbc}): {count}")

a_even = tuple(i for i in a if i % 2 == 0)
a_odd = tuple(i for i in a if i % 2 != 0)
print(f"Tuple cac so chan trong A: {a_even}")
print(f"Tuple cac so le trong A: {a_odd}")

print("Nhap mot ky tu k: ")
k = input()
count_k = sum(s.count(k) for s in b)
print(f"So lan xuat hien cua ky tu '{k}' trong B: {count_k}")

b_long = tuple(i for i in b if len(i) >= 5)
print(f"Cac phan tu trong B co do dai >= 5 ky tu: {b_long}")

c = tuple((a[i], b[i]) for i in range(min(len(a), len(b))))
print(f"Tuple C (ket hop A va B): {c}")
