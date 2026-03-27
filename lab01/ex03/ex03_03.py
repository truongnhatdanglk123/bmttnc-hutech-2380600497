def tao_tuple(lst):
    return tuple(lst)

input_list = input("Nhập danh sách số: ")
numbers = [int(x.strip()) for x in input_list.split(",")]

my_tuple = tao_tuple(numbers)

print("List:", numbers)
print("Tuple:", my_tuple)