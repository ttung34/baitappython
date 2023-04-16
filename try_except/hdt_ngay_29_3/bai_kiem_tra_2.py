class Khoi_tao():
    def __init__(self, mon, tin_chi):
        self.mon = mon
        self.tin_chi = tin_chi

    def print_thong_tin(self):
        print(f"Mon hoc:{self.mon}: tin chi:{self.tin_chi}")

class Mon_hoc():
    def __init__(self):
        self.bang_dang_ky = []

    def them_mon_hoc(self):
        for i in range(5):
            mon = input("Nhap ten mon hoc: ")
            tin_chi = int(input(f"Nhap so tin chi cua {mon}: "))
            new_mon = Khoi_tao(mon,tin_chi)
            self.bang_dang_ky.append(new_mon)
            
    
    def print_mon_hoc(self):
        for mon in self.bang_dang_ky:
            mon.print_thong_tin()
            # print(mon.mon)
            # print(mon.tin_chi)
# mon = Mon_hoc()
# mon.them_mon_hoc()
# mon.print_mon_hoc()

class Chon_mon_hoc():
    def __init__(self):
        self.mon_da_chon = {}
    
    def mon_chon(self,mon_hoc):
        while True:
            print("Danh sach mon hoc va tin chi")
            mon_hoc.print_mon_hoc()
            print(self.mon_da_chon)
            mon_ban_dang_ky = input("Nhap mon ban muon dang ky va nhap end de ket thuc: ")
            if mon_ban_dang_ky == "end":
                break
            else:
                for mon in mon_hoc.bang_dang_ky:
                    if mon.mon == mon_ban_dang_ky:
                        print(type(mon.mon))
                        credit = int(input('Nhap gia tien mot tin: '))
                        if mon.mon not in self.mon_da_chon:
                            self.mon_da_chon[mon.mon]= {"credit":0, "tin_chi":mon.tin_chi }
                        self.mon_da_chon[mon]["credit"] += credit
        total = 0                
        for mon_hoc_chon, mon_tin_chi in self.mon_da_chon.items():
            credit = mon_tin_chi["credit"]
            tin_chi = mon_tin_chi["tin_chi"]
            total += credit*tin_chi
            print(f"{mon_hoc_chon}:{tin_chi}*{credit} = {tin_chi*credit}")
        print(f"Tong so tien ban phai tra cho ki nay la {total}")

mon = Mon_hoc()
mon.them_mon_hoc()
mon.print_mon_hoc()
chon =Chon_mon_hoc()
chon.mon_chon(mon)