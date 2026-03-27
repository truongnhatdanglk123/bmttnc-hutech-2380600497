input_str = input("Nhập X,Y: ")
dims = [int(x) for x in input_str.split(",")]

row = dims[0]
col = dims[1]

matrix = []

for i in range(row):
    hang = []
    for j in range(col):
        hang.append(i * j)
    matrix.append(hang)

print(matrix)