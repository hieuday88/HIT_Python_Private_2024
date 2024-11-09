
k = int(input("Nhập số phần tử k = "))
a = [int(input(f'Nhập a[{i}] = ')) for i in range(k)]

n = int(input("Nhập n = "))
m = int(input("Nhập m = "))

if k >= n * m:
    X = [a[i * m:(i + 1) * m] for i in range(n)]
    print(X)
else:
    print("Không thể xây dựng được ma trận.")
