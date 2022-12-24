from datetime import datetime


class Product:
    def __init__(self, name, price, stock, desc):
        self.name = name
        self.price = int(price)
        self.stock = int(stock)
        self.description = desc

    def __str__(self):
        return f'{self.name}, price: {self.price}'


class Customer:
    def __init__(self, first_name, last_name, phone_num, city):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.city = city

    def __str__(self):
        return f'Customer: {self.last_name} {self.first_name[0]}. {self.city} {self.phone_num}'


class Order():
    def __init__(self, customer, product, qty):
        self.customer = customer
        self.product = product
        self.quantity = qty

    def amount(self):
        if not self.product.stock:
            raise ValueError(f'{self.product} is out of stock')
        elif self.quantity > self.product.stock:
            raise ValueError(f'The required quantity of {self.product} is more that available on stock')
        else:
            self.product.stock = int(self.product.stock) - int(self.quantity)
            self.amount = self.quantity * self.product.price
            return self.amount

    def __str__(self):
        return f'ORDER\nDate: {datetime.today().replace(microsecond=0)}\n' \
               f'{self.customer}\n{self.product.name} {self.product.description}:' \
               f' {self.quantity} unit(s)\n' \
               f'Amount to pay: {self.amount()}'


mobile_1 = Product('iPhone 13', '41_999', '3', '256GB, Starlight')
mobile_2 = Product('iPhone 14 Plus', '51_999', '2', '256GB, Purple')
mobile_3 = Product('iPhone 14 Plus', '61_999', '1', '516GB, Purple')
mobile_4 = Product('iPhone14 Pro', '64_999', '0', '256GB Deep Purple')

customer_1 = Customer('Olga', 'Telizhuk', '0958023959', 'Kyiv')

orders = []

order1 = Order(customer_1, mobile_1, 2)
order2 = Order(customer_1, mobile_2, 2)
order3 = Order(customer_1, mobile_3, 2)
order4 = Order(customer_1, mobile_4, 2)


print(order1)
print(f'Stock of {order1.product} upon order acceptance: {order1.product.stock}')
print('=' * 50)
print(order2)
print(f'Stock of {order2.product} upon order acceptance: {order2.product.stock}')
print('=' * 50)
print(order3)
print(f'Stock of {order3.product} upon order acceptance: {order3.product.stock}')
print('=' * 50)
print(order4)
print(f'Stock of {order4.product} upon order acceptance: {order4.product.stock}')

