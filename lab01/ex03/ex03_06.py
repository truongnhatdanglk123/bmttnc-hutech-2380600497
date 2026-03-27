def xoa_key(d, key):
    if key in d:
        del d[key]
        return True
    return False

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

key = input("Nhập key cần xóa: ")

if xoa_key(my_dict, key):
    print("Dictionary sau khi xóa:", my_dict)
else:
    print("Không tìm thấy key")