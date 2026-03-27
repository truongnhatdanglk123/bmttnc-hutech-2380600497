def dem_so_lan_xuat_hien(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

input_str = input("Nhập danh sách: ")
words = [x.strip() for x in input_str.split(",")]

result = dem_so_lan_xuat_hien(words)

print("Số lần xuất hiện:", result)