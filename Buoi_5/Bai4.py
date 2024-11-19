import random

n = int(input("Nhap so luong tai khoan: "))
danhsach_taikhoan = {}

loai_matkhau = ['CNTT', 'KHMT', 'KTPM', 'HTTT', 'DAPT']

for i in range(1, n + 1):
    masinhvien = f"202360{str(i).zfill(4)}"
    matkhau = random.choice(loai_matkhau) + masinhvien

    danhsach_taikhoan[f'Account{i}'] = {
        "Username": masinhvien,
        "Password": matkhau
    }

print(danhsach_taikhoan)
