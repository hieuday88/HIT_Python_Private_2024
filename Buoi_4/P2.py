n = int(input("Nhập số phần tử n = "))
a = [input(f'Nhập a[{i}] = ') for i in range(n)]
m = int(input("Nhập số phần tử m = "))
b = [input(f'Nhập b[{i}] = ') for i in range(m)]

c = []
i, j = 0, 0

while i < n and j < m:
    c.append(a[i])
    c.append(b[j])
    i += 1
    j += 1
while i < n:
    c.append(a[i])
    i += 1
while j < m:
    c.append(b[j])
    j += 1

print(c)
