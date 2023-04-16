class Shop:
    def __init__(self):
        self.hoa_don = []
        self.tong =0
        
    def mua_hang(self):
        print("Nhap 1 de mua hang, nhap 2 la ban khong co mon hang ban can")
        choice = int(input("Hay nhap so ban muon: "))
        if choice == 1:
            so_hang_hoa_mua = int(input("Hay nhap so do muon mua: "))
            for a in range (so_hang_hoa_mua):
                ten_hang_hoa = input("Hay nhap ten hang do: ")
                so_luong_mua = int(input(f"Hay nhap so luong {ten_hang_hoa} ma ban muon mua: "))
                gia_tien = int(input("Hay nhap gia tien: "))
                self.hoa_don.append(ten_hang_hoa)
                self.hoa_don.append(so_luong_mua)
                self.hoa_don.append(gia_tien)
        if choice == 2 :
            print ("Cam on ban da lua chon chung toi, rat mong se duocj phuc vu ban trong mot lan gan nhat: ")

    def sum(self):
            for i in range (0,len(self.hoa_don),3):
                total = self.hoa_don[i+1]*self.hoa_don[i+2]
            self.tong = total
    
    def in_fo(self):
        for i in range(0,len(self.hoa_don),3):
            print(f"{self.hoa_don[i]}:{self.hoa_don[i+1]}:{self.hoa_don[i+2]}")
        print(f"Ban can phai tra {self.tong}")
        
shop1 = Shop ()
shop1.in_fo()
shop1.mua_hang()
shop1.sum()
        