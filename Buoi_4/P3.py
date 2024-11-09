
n = int(input("Nhập số phần tử của nums1: "))
nums1 = [int(input(f'Nhập nums1[{i}] = ')) for i in range(n)]

m = int(input("Nhập số phần tử của nums2: "))
nums2 = [int(input(f'Nhập nums2[{i}] = ')) for i in range(m)]

nums3 = []

for num in nums1:
    if num in nums2:
        nums3.append(num)
        nums2.remove(num)

print("Kết quả:", nums3)




