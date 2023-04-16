import random

def san_sinh_mang_ngau_nhien(n):
    mang = []
    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)
    
    return mang

def sap_xep_chon(mang):
    n = len(mang)

    for i in range(n-1):
        vi_tr_min = i

        for j in range(i+1,n):
            if mang[vi_tr_min]>mang[j]:
                vi_tr_min = j
        
        mang[i],mang[vi_tr_min]=mang[vi_tr_min],mang[i]
        print(i," ",mang) 
       

def main():
    mang = san_sinh_mang_ngau_nhien(10)
    print('Mang ban dau la:\n',mang) 
    sap_xep_chon(mang)
    print("Mang sau khi sap xep la\n", mang) 

if __name__ == "__main__":
    main()