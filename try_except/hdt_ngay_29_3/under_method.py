class Product:
    def __init__(self):
        self.name = input("Nhập tên đồ uống: ")
        self.price = int(input("Nhập giá đồ uống: "))
    def print_product(self):
        print(f"{self.name} giá {self.price}")
    def update_price(self, new_price):
        self.price = new_price
    def update_name(self, new_name):
        self.name = new_name
class Product_list:
    def __init__(self):
        self.product_list = []
    def add_product(self):
        name = input("Hãy nhập tên đồ uống: ")
        price = int(input("Nhập giá đồ uống: "))
        new_product = Product
        self.product_list.append(new_product)
    def print_product(self):
        for product in self.product_list:
            product.print_product()
    def delete_product(self):
        product_remove = input("Nhập sản phẩm muốn xóa: ")
        for product in self.product_list:
            if product_remove == product.name:
                self.product_list.remove(product)
            else:
                print("Đồ uống ko có trong menu")
    def update_product(self):
        product_update = input("Nhập đồ uống cần sửa: ")
        check = 0
        for product in self.product_list:
            if product.name() == product_update:
                new_name = input("Nhập đồ uống mới: ")
                new_price = input("Nhập giá mới: ")
                product.update_name(new_name)
                product.update_price(new_price)
                check = 1
        if check == 0:
            print("Sản phẩm không có trong danh sách")
class Bill():
    def __init__(self):
        self.buy = {}
        self.total = 0
    def buy(self, product_list):
        while True:
            print("*****MENU*****")
            product_list.print_product()
            buy_product = input("Nhập đồ uống bạn muốn mua (q để thoát chương trình): ")
            if buy_product == "q":
                break
            else:
                for product in product_list.product_list:
                    if buy_product == product.name:
                        so_luong = int(input("Số lượng: "))
                        if product.name not in self.buy:
                            self.buy[product.name] = {"so_luong": 0, "price": product_price}
                        self.buy[product.name]["so_luong"] += so_luong


product_List = Product_list()
product_List.add_product()
product_List.add_product()
product_List.update_product()
product_List.delete_product()
bill = Bill()