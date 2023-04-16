n = int(input("Nhap so phan tu trong day: "))
a = list(map(int,input("Nhap day so: ")))
x = int(input("Nhap phan tu can tim: "))
mid = -1
for i in range(len(a)):
    l=0
    r=n-1
    mid=int(l+((r-l)*(x-a[l]))/(a[r]-a[l]))
    if  a[mid]<x:
        l=mid+1
    else:
        if a[mid]==x:
            break
        else:
            if a[mid]>x:
                r=mid-1
        
print(f"Chi so can tim la: {mid}")