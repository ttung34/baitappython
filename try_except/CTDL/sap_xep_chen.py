import random

def san_sinh_so_ngau_nhien(n):
    mang =[]
    
    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)

    return mang

def sap_xep_chen(mang):
    n = len(mang)

    for i in range(1,n):
        tam = mang[i]
        j =i
        
        while j >0 and mang[j-1]>tam:
            mang[j]=mang[j-1]
            j =j-1
            # 0
        # print(i," ", mang)
    
        mang[j] = tam
        print(i," ", mang)

def main():
    mang = san_sinh_so_ngau_nhien(10)
    print(f"Mang ban dau la {mang}")
    sap_xep_chen(mang)
    print(f"Mang luc sau la {mang}")

if __name__ == "__main__":
    main()