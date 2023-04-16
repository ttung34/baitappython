# The Product class is used to display the list of products and their prices. 
# The Invoice class is used to buy products and print the invoice
class Product:
    def __init__(self):
        self.products = {}
    def display_info(self):
        products = {
            'Táo': 8000,
            'CoCa': 10000,
            'Trà Sữa': 30000,
            'Caffe': 35000
        }
        for product in products:
            print(f'{product}: {products[product]} VNĐ')

class Invoice:
    def __init__(self):
        self.cart = {}

    def buy(self):
        products = {
            'Táo': 8000,
            'CoCa': 10000,
            'Trà Sữa': 30000,
            'Caffe': 35000
        }
        while True:
            buy = input('Bạn muốn mua hàng hoá gì (nhập "done" để tính tiền): ')
            if buy == 'done':
                break
            if buy in products:
                quantity = int(input("Bạn muốn mua bao nhiêu: "))
                print(f'Đã thêm {buy} vào giỏ hàng')
                print('-' * 25)
                self.add_to_cart(buy, quantity)
            else:
                print('Hàng hoá không tồn tại')
        self.print_invoice(products)

    def add_to_cart(self, product, quantity):
        if product not in self.cart:
            self.cart[product] = quantity
        else:
            self.cart[product] += quantity

    def print_invoice(self, products):
        print('-' * 25)
        print('Hoá Đơn:')
        total_price = 0
        for product, quantity in self.cart.items():
            price = products[product] * quantity
            total_price += price
            print(f'{product}: {quantity} x {products[product]} VND = {price} VND')
        print(f'Tổng tiền hoá đơn là: {total_price} VND')

product = Product()
print(f"Danh sách hàng hoá và giá bán:")
print('-' * 25)
product.display_info()
print('-' * 25)
invoice = Invoice()
invoice.buy()