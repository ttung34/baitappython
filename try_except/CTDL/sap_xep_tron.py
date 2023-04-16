import random

def san_sinh_so_ngau_nhien(n):
    mang =[]

    for i in range(n):
        so_ngau_nhien = random.randint(0,100)
        mang.append(so_ngau_nhien)

    return mang

def sap_xep_tron(mang):
    if len(mang) >1:
        giua =len(mang)//2
        mang_trai = mang[:giua]
        mang_phai = mang[giua:]
        
        sap_xep_tron(mang_trai)
        sap_xep_tron(mang_phai)

        i = j =k = 0
        while(i<len(mang_trai) and j<len(mang_phai)):
            if mang_trai[i]<mang_phai[j]:
                mang[k] = mang_trai[i]
                i+=1
            else:
                mang[k]=mang_phai[j]
                j+=1
            k+=1
        #     print(i,"-", mang)
        #     print(j,"-", mang)
        #End While
        
        # These while loops are used to merge the two sorted sub-arrays (mang_trai and mang_phai) into
        # a single sorted array (mang).
        while i<len(mang_trai):
            mang[k]= mang_trai[i]
            i+=1
            k = k =k+1
        #End while
        
        while j<len(mang_phai):
            mang[k]= mang_phai[j]
            j+=1
            k+=1
        #End While
    print("-",mang)
#End Def
def main():
    mang =san_sinh_so_ngau_nhien(10)
    print(f"Mang ban dau la: {mang}")
    sap_xep_tron(mang)
    print(f"Sau khi sap xep la: {mang}")

if __name__ =="__main__":
    main()