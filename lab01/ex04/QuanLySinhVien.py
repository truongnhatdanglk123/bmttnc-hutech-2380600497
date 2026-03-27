from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        if len(self.listSinhVien) == 0:
            return 1
        return max(sv._id for sv in self.listSinhVien) + 1

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        id = self.generateID()
        name = input("Tên: ")
        sex = input("Giới tính: ")
        major = input("Ngành: ")
        diemTB = float(input("Điểm TB: "))

        sv = SinhVien(id, name, sex, major, diemTB)
        self.xepHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, id):
        sv = self.findByID(id)
        if sv:
            sv._name = input("Tên mới: ")
            sv._sex = input("Giới tính: ")
            sv._major = input("Ngành: ")
            sv._diemTB = float(input("Điểm TB: "))
            self.xepHocLuc(sv)
        else:
            print("Không tìm thấy!")

    def deleteByID(self, id):
        sv = self.findByID(id)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False

    def findByID(self, id):
        for sv in self.listSinhVien:
            if sv._id == id:
                return sv
        return None

    def findByName(self, name):
        return [sv for sv in self.listSinhVien if name.lower() in sv._name.lower()]

    def sortByDiem(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    def xepHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def show(self):
        print("\nDanh sách sinh viên:")
        for sv in self.listSinhVien:
            print(sv)