class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def print_info(self):
        print(f"{self.name} --- {self.price}")
    
    def update_price(self, new_price):
        self.price = new_price
        
    def update_name(self, new_name):
        self.name = new_name
    
class ProductList:
    def __init__(self):
        self.product_list = []
        
    def add_product(self):
        name = input("Hãy nhập tên hàng hoá: ")
        price = int(input("Hãy nhập giá hàng hoá: "))
        new_product = Product(name, price)  
        self.product_list.append(new_product)
    
    def print_info(self):
        for product in self.product_list:
            print(product)
            product.print_info()
    
    def delete_product(self):
        product_want_delete = input('Nhập sản phẩm muốn xóa: ')
        for product in self.product_list: 
            if product_want_delete == product.name:
                self.product_list.remove(product)
            else:
                print('Sản phẩm bạn nhập không có trong menu')
    
    def update_product(self):
        product_want_update = input("Nhập tên sản phẩm cần đổi: ")
        check = 0
        for product in self.product_list:
            if product.name == product_want_update:
                print("dday laf",product.name)

                new_name = input("Nhập tên mới: ")
                new_price = int(input("Nhập giá mới: "))
                product.update_name(new_name)
                product.update_price(new_price)
                check = 1
        if check==0:
                print("Sản phầm không có trong danh sách")
class Bill():
    def __init__(self):
        self.buying = {}
    
    def buy(self, product_list):
        while True:
            print("Danh sách sản phẩm:")
            print(self.buying)
            product_list.print_info()
            buy_product = input("Nhập tên sản phẩm bạn muốn mua (nhấn q để thoát): ")
            if buy_product == 'q':
                break
            else:
                # A for loop. It will loop through all the products in the product list.
                for product in product_list.product_list:
                    if product.name == buy_product:
                        quantity = int(input("Nhập số lượng: "))
                        if product.name not in self.buying:
                            self.buying[product.name] = {"quantity": 0, "price": product.price}
                        self.buying[product.name]["quantity"] += quantity
                        print(self.buying)
        print("-"*20)                
        print("Hóa đơn mua hàng")
        total_price = 0   
        for product_name, product_info in self.buying.items ():
            quantity = product_info["quantity"]
            price = product_info["price"]
            total_price += quantity * price
            print(f"{product_name}: {quantity} x {price} = {quantity * price}")
            
        print(f"Tổng tiền: {total_price}")
    
product_list_1 = ProductList()
print("-"*20)
product_list_1.add_product()
product_list_1.add_product()
product_list_1.update_product()
product_list_1.delete_product()
bill = Bill()
print("-"*20)
bill.buy(product_list_1)
# def main():
#     i = 1
#     product_list_1 = ProductList()
#     bill = Bill()
#     while i != 0 :
#         if i == 1:
#             product_list_1.add_product()
#         elif i ==2 :
#             product_list_1.update_product()
#         elif i ==3 :
#             bill.buy(product_list_1)
#         i = input("Nhap uu cau: ")      
        


    

    # product_list_1 = ProductList()
    # print("-"*20)
    # product_list_1.add_product()
    # product_list_1.add_product()
    # product_list_1.update_product()
    # product_list_1.delete_product()
    # bill = Bill()
    # print("-"*20)
#     # bill.buy(product_list_1)

# if __name__ == "__main__":
#     main()