a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

print("a*b= ", a * b)
print("a+b= ", a + b)
print("a-b=", a - b)
print("a/b= ", a / b)
print("a**b=", a ** b)
print("a//b=", a // b)
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a == b")
print("a and b: ", a and b)
print("a or b : ", a or b)
print(f"a ^ b = {a ^ b}")
print(f"NOT (a == b) = {not (a == b)}")
print(f"a >> 5 = {a >> 5}")
print(f"a << 6 = {a << 6}")

br = bin(a)[2:][::-1]
print(f"Hệ cơ số 2 đảo ngược của a: {br}")