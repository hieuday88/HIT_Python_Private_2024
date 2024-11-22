n = 1000
x = int(input("x = "))
def gt(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

e = 1
for i in range(1,n+1):
    e += x**i/gt(i)

print(e)