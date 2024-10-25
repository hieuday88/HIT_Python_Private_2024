# a
print("Chao mung den CLB Tin Hoc HIT")

# b
print("CLB Tin Hoc HIT truc thuoc Khoa CNTT - “10 diem”")

# c
chuoi = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
chu_cai_hoa = [char for char in chuoi if char.isupper()]
print("Chữ in hoa trong chuỗi:", "".join(chu_cai_hoa))

# d
chu_cai_thuong = [char for char in chuoi if char.islower()]
print("Chữ thường trong chuỗi:", "".join(chu_cai_thuong))

# e
if "CNTT" in chuoi:
    print("Yes")
else:
    print("No")

# f
chuoi_thay_doi = chuoi.swapcase()
print("Chuỗi sau khi thay đổi:", chuoi_thay_doi)
