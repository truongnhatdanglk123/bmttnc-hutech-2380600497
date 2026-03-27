def lay_dau_cuoi(t):
    return t[0], t[-1]

input_tuple = tuple(map(int, input("Nhập tuple: ").split(",")))

first, last = lay_dau_cuoi(input_tuple)

print("Phần tử đầu:", first)
print("Phần tử cuối:", last)