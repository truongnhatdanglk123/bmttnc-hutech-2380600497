def dao_nguoc(s):
    return s[::-1]

chuoi = input("Nhập chuỗi: ")
print("Chuỗi đảo:", dao_nguoc(chuoi))