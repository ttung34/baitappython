danh_sach_hoc_phan_CNTT ={}
danh_sach_hoc_phan_KHDL ={}
def nhap_thong_tin_hoc_phan(chuong_trinh):
    ten_hoc_phan = input("Nhap ten hoc phan moi: ")
    chuong_trinh[ten_hoc_phan]= int(input(f'Nhap so tin chi cua hoc phan {ten_hoc_phan}: '))

def in_cac_hoc_phan(chuong_trinh):
    for hoc_phan in chuong_trinh:
        print(f"{hoc_phan}: {chuong_trinh[hoc_phan]} tin chi")

print("Hay nhap hoc phan cua nghanh CNTT")
for i in range (3):
    nhap_thong_tin_hoc_phan(danh_sach_hoc_phan_CNTT)

print("Hay nhap hoc phan cua nghanh KHDL")
for i in range (3):
    nhap_thong_tin_hoc_phan(danh_sach_hoc_phan_KHDL)

chuong_trinh_dao_tao = input("Hay nhap chuong trinh dao tao ban muon: ")
danh_sach_ban_da_chon = {}
if (chuong_trinh_dao_tao == "CNTT"):
    in_cac_hoc_phan(danh_sach_hoc_phan_CNTT)
    so_mon_muon_dang_ky = int(input("Nhap so mon ban muon dang ky: "))
    for i in range(so_mon_muon_dang_ky):
        hoc_phan_da_chon = input("Hay nhap ten mon hoc ban muon dang ky: ")
        for ten_mon in danh_sach_hoc_phan_CNTT:
            if ten_mon.ten_hoc_phan == hoc_phan_da_chon:
                price = 320000 
                if ten_mon.ten_hoc_phan not in so_mon_muon_dang_ky:
                    so_mon_muon_dang_ky[hoc_phan_da_chon]= {"tin chi":danh_sach_hoc_phan_CNTT[hoc_phan_da_chon],"gia tien":0}
                so_mon_muon_dang_ky[hoc_phan_da_chon]["gia tien"]+= price

#         ten_phai_nop = danh_sach_hoc_phan_CNTT[hoc_phan_da_chon]*320000
#         print(f"Ban da dang ky hoc {hoc_phan_da_chon}-{danh_sach_hoc_phan_CNTT[hoc_phan_da_chon]}")
#         print(f"So tien ban phai dong la: {ten_phai_nop}")
# if (chuong_trinh_dao_tao == "KHDL"):
#     in_cac_hoc_phan(danh_sach_hoc_phan_KHDL)
#     hoc_phan_da_chon = input("Hay nhap ten mon hoc ban muon dang ky: ")
#     ten_phai_nop = danh_sach_hoc_phan_KHDL[hoc_phan_da_chon]*320000
#     print(f"Ban da dang ky hoc {hoc_phan_da_chon}-{danh_sach_hoc_phan_KHDL[hoc_phan_da_chon]}")
#     print(f"So tien ban phai dong la: {ten_phai_nop}")