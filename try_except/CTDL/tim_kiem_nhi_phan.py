import random #San sinh so ngau nhien

def san_sinh_mang_tang_dan(n):
    mang=[]
    
    so_dau_tien = random.randint(0,100)
    mang.append(so_dau_tien)
    
    for i in range(1,n):
        tang = random.randint(1,10)
        so = mang[i-1]+tang
        mang.append(so)

    return mang

#ham nhan vao tham so mang la danh sach cac so da duocj sap xep theo thu tu tang dan
#Ham nhan vao tham so x la gia tri can tim
#Ham tra ve vi tri tim duoc
def tim_nhi_phan(mang,x):
    trai= 0
    phai= len(mang)-1
  
    while trai<phai:
        giua = (trai+phai)//2

        if mang[giua] == x:
            return giua
        
        if x<mang[giua]:
            phai =giua-1
        else:
            trai = giua +1

    return -1

def main(): #dinh nghia ham
    mang = san_sinh_mang_tang_dan(20)
    print(mang)

    x = int(input(f"Nhap vao gia tri so nguyen can tim: "))

    vi_tri = tim_nhi_phan(mang,x)

    if vi_tri!=-1:
        print(f"Gia tri {x} duoc tim thay tai vi tri {vi_tri}")
    else:
        print(f'Khong tim thay gia tri {x} trong mang')

if __name__ == "__main__":#Goi thuc hien ham chinh khi modun ching cua chuong trinh
    main()