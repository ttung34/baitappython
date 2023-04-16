import random

def san_sinh_so_ngau_nhien(n):
    mang=[]

    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)

    return mang

def sap_xep_noi_bot(mang):
    n = len(mang)

    for i in range(n):
        tiep_tuc = False

        for j in range(n-2,i-1,-1):# j thuoc =[n-2,i]
            if mang[j]>mang[j+1]:
                mang[j], mang[j+1] = mang[j+1],mang[j]
                tiep_tuc=True

        print(i,'-',mang)

        if tiep_tuc == False:
            break

def main():
    mang = san_sinh_so_ngau_nhien(10)
    # mang=[1,3,4,5,7,8,10,19]
    print(f'Mang ban dau la: {mang}')
    sap_xep_noi_bot(mang)
    print(f"Mang sau khi sap xep la: {mang}")

if __name__ =="__main__":
    main()