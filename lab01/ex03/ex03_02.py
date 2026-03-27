def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("Nhập danh sách số: ")
numbers = [int(x.strip()) for x in input_list.split(",")]

print("List đảo ngược:", dao_nguoc_list(numbers))