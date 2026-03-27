so_gio = float(input("Nhập số giờ làm: "))
luong_gio = float(input("Nhập lương/giờ: "))

gio_chuan = 44
gio_them = max(0, so_gio - gio_chuan)

thuc_linh = gio_chuan * luong_gio + gio_them * luong_gio * 1.5

print("Lương nhận được:", thuc_linh)