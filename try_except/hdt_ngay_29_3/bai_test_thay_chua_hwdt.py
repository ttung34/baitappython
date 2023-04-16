class Hoc_phan():
    def __init__(self):
        self.ten_mon_hoc = input("Hay nhap ten hoc phan: ")
        self.so_tin_chi = int(input(f"Hay nhap so tin chi cua {self.ten_mon_hoc}: "))
    
    def print_infor(self):
        print(f"{self.ten_mon_hoc}--{self.so_tin_chi}")

class Danh_sach_hoc_phan():
    def __init__(self):
        self.name = input("Nhap ten nghanh hoc: ")
        self.danh_sach =[]
    
    def add_new_subject(self):
        so_mon_ban_muon_them = int(input(f"Nhap so mon ban muon them vo cho nganh {self.name}: "))
        for i in range(so_mon_ban_muon_them):
            self.danh_sach.append(Hoc_phan())
            

    def print_infor(self):
        print(f"Danh sach nganh cua ban {self.name}")
        for hoc_phan in self.danh_sach:
            hoc_phan.print_infor()
            # print(hoc_phan)
            # print(self.danh_sach)

class Student:
    def __init__(self):
        self.name = input("Nhap ten cua sinh vien: ")
        self.nganh_hoc = input("Nhap ten nganh hoc cua sinh vien: ")
        self.hoc_phan_da_dang_ky =[]

    def in_danh_sach_hoc_phan_da_dang_ky(self):
        print("-----Danh sach hoc phan da dang ky------")
        for hoc_phan in self.hoc_phan_da_dang_ky:
            hoc_phan.print_infor()
    
    def tinh_tien(self):
        tien_phai_nop =0
        for hoc_phan in self.hoc_phan_da_dang_ky:
            tien_phai_nop+=hoc_phan.so_tin_chi*320000
            print(hoc_phan.so_tin_chi)
        print(f"Tong so tien phai dong la: {tien_phai_nop}")

danh_sach_hoc_phan_CNTT = Danh_sach_hoc_phan()
danh_sach_hoc_phan_CNTT.add_new_subject()
danh_sach_hoc_phan_CNTT.print_infor()

danh_sach_hoc_phan_KHDL = Danh_sach_hoc_phan()
danh_sach_hoc_phan_KHDL.add_new_subject()
danh_sach_hoc_phan_KHDL.print_infor()

student_1=Student()
if (student_1.nganh_hoc == "CNTT"):
    danh_sach_hoc_phan_CNTT.print_infor()
    so_mon_ban_muon_dang_ky = int(input("Nhap so mon ban muon dang ky: "))
    for i in range(so_mon_ban_muon_dang_ky):
        hoc_phan_dan_chon = input("Nhap ten hoc phan: ")
        for hoc_phan in danh_sach_hoc_phan_CNTT.danh_sach:
            if(hoc_phan_dan_chon == hoc_phan.ten_hoc_phan):
                student_1.hoc_phan_da_dang_ky.append(hoc_phan)

if (student_1.nganh_hoc == "KHDL"):
    danh_sach_hoc_phan_KHDL.print_infor()
    so_mon_ban_muon_dang_ky = int(input("Nhap so mon ban muon dang ky: "))
    for i in range(so_mon_ban_muon_dang_ky):
        hoc_phan_dan_chon = input("Nhap ten hoc phan: ")
        for hoc_phan in danh_sach_hoc_phan_KHDL.danh_sach:
            if(hoc_phan_dan_chon == hoc_phan.ten_hoc_phan):
                student_1.hoc_phan_da_dang_ky.append(hoc_phan)


student_1.in_danh_sach_hoc_phan_da_dang_ky()
student_1.tinh_tien()