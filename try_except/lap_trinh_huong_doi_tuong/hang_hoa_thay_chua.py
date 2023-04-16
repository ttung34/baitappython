class Product:
    def __init__(self, name, price):
        self.name = name
        self.price =price

    def print_info(self):
        print(f"{self.name}--{self.price}")

    def update_name(self, new_name):
        self.name = new_name

    def update_price(self, new_price):
        self.price = new_price

class ProductList:
    def __init__(self):
        self.product_list = []

    def add_product(self):
        name = input("Nhap ten san pham: ")
        price = int(input(f"Nhap gia cua {name}: "))
        new_product = Product(name, price)
        self.product_list.append(new_product)
    
    def print_info(self):
        for product in self.product_list:
            product.print_info()

    def update_product(self):
        print("Nhap 1 neu ban muon update, nhap 2 ban khong muon update")
        check = int(input("So ban muon nhap vo: "))
        if check == 1 :
            so_luong_update = int(input("So san pham ban muon update"))
            for i in range(0, len(so_luong_update)):
                for product in self.product_list:
                    new_name = input("Nhap ten san pham moi: ")
                    new_price = int(input(f"Nhap gia tien cua {new_name}: "))
                    product.update_name(new_name)
                    product.update_price(new_price)
        if check == 2:
            print("Ban khong can phai update san pham nao ca")

class Bill():
    def __init__(self):
        self.bill = {}

    def buy(self, product_list):
        product_list.print_info()
        while True:
            san_pham = input("Nhap ten san pham ban muon mua(nhap q neu ban khong co sua lua chon): ")
            if san_pham == "q" :
                break
            else: 
                for product in product_list.product_list:
                    if product.name == san_pham:
                        so_luong = int(input("So luong ban muon mua: "))
                        if product.name not in self.bill:
                            self.bill[product.name] ={"so luong":0, "price": product.price}
                        self.bill[product.name]["so_luong"]+= so_luong
        print("Hoa don mua hang")
        total_price = 0
        for product_name, product_so_luong in self.bill.items():
            so_luong = product_so_luong["so_luong"]
            pirce = product_so_luong["price"]
            total_price += so_luong * pirce
            print(f"{product_name}:{so_luong}x{pirce} = {so_luong*pirce}")

        print(f"tong tien: {total_price}") 

product_list_1 = ProductList()
print("-"*20)
product_list_1.add_product()
product_list_1.add_product()
product_list_1.update_product()

bill = Bill()
print("-"*20)
bill.buy(product_list_1)
