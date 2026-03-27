from QuanLySinhVien import QuanLySinhVien

ql = QuanLySinhVien()

while True:
    print("\n===== MENU =====")
    print("1. Thêm sinh viên")
    print("2. Cập nhật sinh viên")
    print("3. Xóa sinh viên")
    print("4. Tìm theo tên")
    print("5. Sắp xếp theo điểm")
    print("6. Sắp xếp theo tên")
    print("7. Hiển thị danh sách")
    print("0. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        ql.nhapSinhVien()

    elif choice == "2":
        id = int(input("Nhập ID: "))
        ql.updateSinhVien(id)

    elif choice == "3":
        id = int(input("Nhập ID: "))
        if ql.deleteByID(id):
            print("Đã xóa")
        else:
            print("Không tìm thấy")

    elif choice == "4":
        name = input("Nhập tên: ")
        result = ql.findByName(name)
        for sv in result:
            print(sv)

    elif choice == "5":
        ql.sortByDiem()
        print("Đã sắp xếp theo điểm")

    elif choice == "6":
        ql.sortByName()
        print("Đã sắp xếp theo tên")

    elif choice == "7":
        ql.show()

    elif choice == "0":
        break

    else:
        print("Sai lựa chọn!")