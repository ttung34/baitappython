# A menu for the user to choose what they want to do.
check = int(input("Hay nhap so b muon chon:"))
if check == 1:
    class shop:
        def __init__(self):
            self.hoa_don = []
            self.tong=0

        def sum(self):
            for i in range (0,len(self.hoa_don),3):
                total = self.hoa_don[i+1]*self.hoa_don[i+2]
            self.tong = total
        
        def new_hang_hoa(self):
            so_hang_hoa_mua = int(input("Hay nhap so do muon mua: "))
            for a in range (so_hang_hoa_mua):
                ten_hang_hoa = input("Hay nhap ten hang do: ")
                so_luong_mua = int(input(f"Hay nhap so luong {ten_hang_hoa} ma ban muon mua: "))
                gia_tien = int(input("Hay nhap gia tien: "))
                self.hoa_don.append(ten_hang_hoa)
                self.hoa_don.append(so_luong_mua)
                self.hoa_don.append(gia_tien)

        def in_fo(self):
            for i in range(0,len(self.hoa_don),3):
                print(f"{self.hoa_don[i]}:{self.hoa_don[i+2]}:{self.hoa_don[i+2]}")
            print(f"Ban can phai tra {self.tong}")
    
    shop1 = shop ()
    shop1.in_fo()
    shop1.new_hang_hoa()
    shop1.sum()

if check == 2:
    print("Cam on ba da lua chon cua hang chung toi")  
