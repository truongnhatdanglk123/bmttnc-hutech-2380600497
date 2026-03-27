lines = []

while True:
    line = input("Nhập (gõ 'done' để kết thúc): ")
    if line.lower() == "done":
        break
    lines.append(line)

print("Kết quả:")
for line in lines:
    print(line.upper())