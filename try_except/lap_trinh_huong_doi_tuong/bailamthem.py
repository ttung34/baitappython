class Person:
    def __init__(self):
        self.thong_tin = []

    def info(self):
        so_nguoi_dang_ky =int(input("Hay nhap so nguoi dang ky mang: "))
        for a in range(so_nguoi_dang_ky):
            ten_nguoi_dung =input("Hay nhap ten nguoi dung: ")
            goi_mang = int(input(f'Goi mang ma {ten_nguoi_dung} muon dang ky la: '))
            self.thong_tin.append(ten_nguoi_dung)
            self.thong_tin.append(goi_mang)
    def khuye_mai(self):
        for i in range(0,len(self.thong_tin),2):
            if 60<self.thong_tin[i+1]<90:
                print("Ban duoc mien 5% tien mang")
                tong = self.thong_tin[i+1]-(self.thong_tin[i+1]/100*5)
                self.thong_tin.append(tong)
                for b in range(0,len(self.thong_tin),2):
                    print(f'{self.thong_tin[b]} da dang ky goi mang {self.thong_tin[b+1]} gia phai tra la: {self.thong_tin[b+2]}')
            if self.thong_tin>90:
                print("Ban duoc mien 10% tien mang")
                tong = self.thong_tin[i+1]-(self.thong_tin[i+1]/100*10)
                self.thong_tin.append(tong)
                for c in range(0,len(self.thong_tin),2):
                    print(f'{self.thong_tin[c]} da dang ky goi mang {self.thong_tin[c+1]} gia phai tra la: {self.thong_tin[c+3]}')


people = Person()
people.info()
people.khuye_mai()