n = int(input("Nhap n:"))

input_dict = {}

for i in range(n):
    print("Nhap key:")
    key = input()
    print("Nhap value")
    value = input()
    input_dict[key] = value

swapped_dict = {}
for key,value in input_dict.items():
    swapped_dict[value] = key

if (len(swapped_dict) == n):
    print(swapped_dict)
else:
    print(None)
