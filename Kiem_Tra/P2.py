str_input = input("Nhap 1 xau: ")

result_dict = {}
for k in str_input:
    if k.isalpha():
        k = k.lower()
        if k in result_dict:
            result_dict[k] += 1
        else:
            result_dict[k] = 1

print(result_dict)
