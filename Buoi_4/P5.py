k = int(input("Nhập số phần tử k = "))
print("Nhập dãy sắp tăng dần")
a = [int(input(f'Nhập a[{i}] = ')) for i in range(k)]
key = int(input("Nhập số cần tìm = "))
def binary_search(a,k,key):
    left = 0
    right = k - 1
    while left <= right:
        mid = left + (right - left)//2
        if (a[mid] == key):
            return mid
        elif (a[mid] > key):
            right = mid - 1
        else:
            left = mid + 1
    return -1

print('i =',binary_search(a,k,key))

