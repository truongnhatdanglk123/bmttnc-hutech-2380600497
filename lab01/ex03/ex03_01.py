def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách số (cách nhau dấu phẩy): ")
numbers = [int(x.strip()) for x in input_list.split(",")]

tong = tinh_tong_so_chan(numbers)
print("Tổng số chẵn là:", tong)