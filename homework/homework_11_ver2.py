class Product:

    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} UAH'


class Customer:

    def __init__(self, first: str, last: str, phone: str):
        self.f_name = first
        self.l_name = last
        self.phone = phone

    def __str__(self):
        return f'{self.l_name} {self.f_name} | {self.phone}'


class Order:

    def __init__(self, customer: str):
        self.customer = customer
        self.__products = []  # make attribute private
        self.__quantities = []

    def add_product(self, product: Product, quantity: float = 1):
        if product is self.__products:  # check if the product is in the order
            index = self.__products.index(product)  # update quantity
            self.__quantities[index] += quantity
        else:
            self.__products.append(product)  # add product and quantity
            self.__quantities.append(quantity)

    def amount(self):
        amount = 0
        for index, item in enumerate(self.__products):
            amount += item.price * self.__quantities[index]
        return amount

    # def __str__(self):
    #     res = ''
    #     for index, item in enumerate(self.products):
    #         res += f'{item} x {self.quantities[index]} = {item.price * self.quantities[index]} UAH\n'
    #         return res

    # def __str__(self):
    #     result = ''
    #     for item, quantity in zip(self.products, self.quantities):
    #         result += f'{item} x {quantity} = {item.price * quantity} UAH\n'
    #     return result

    def __str__(self):
        res = '\n'.join(map(
            lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
            zip(self.__products, self.__quantities))
        )
        return f'{self.customer}\n' \
               f'{res}\nTotal: {self.amount()} UAH'


if __name__ == '__main__':
    apple = Product('apple', 20)
    banana = Product('banana', 40)
    orange = Product('orange', 50)

    customer1 = Customer('Olga', 'Telizhuk', '+380958023959')

    order1 = Order(customer1)
    order1.add_product(apple, 2.5)
    order1.add_product(orange, 1.5)
    order1.add_product(banana, 0.7)

    print(apple)
    print(banana)
    print(orange)
    print('=' * 50)
    print(customer1)
    print('=' * 50)
    print(order1)
    print('=' * 50)
    print(order1.__dict__)
    print('=' * 50)
    print(order1._Order__products)
    print(order1._Order__quantities)
