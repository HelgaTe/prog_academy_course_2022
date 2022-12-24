from datetime import datetime
import product
import customer


class Order:
    def __init__(self, customer, prod, qty):
        self.customer = customer
        self.product = prod
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


if __name__ == '__main__':
    mobile_1 = product.Product('iPhone 13', '41_999', '3', '256GB, Starlight')
    mobile_2 = product.Product('iPhone 14 Plus', '51_999', '2', '256GB, Purple')
    mobile_3 = product.Product('iPhone 14 Plus', '61_999', '1', '516GB, Purple')
    mobile_4 = product.Product('iPhone14 Pro', '64_999', '0', '256GB Deep Purple')

    customer_1 = customer.Customer('David', 'Davidov', '0971234567', 'Lviv')

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
