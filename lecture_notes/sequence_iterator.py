x = [1, 2, 3, 4, 5, 6]

it = iter(x)  # __iter__
print(it)
print(next(it))  # __next__ <gets the next item till # StopIteration error>


class Order:
    def __init__(self):
        self.products = []
        self.quantities = []
        self.prices = []

    def add_product(self, product, price, qt=1):
        self.products.append(product)
        self.prices.append(price)
        self.quantities.append(qt)

    def __iter__(self):
        return OrderIter(self.products, self.prices, self.quantities)


class OrderIter:

    def __init__(self, products, prices, qts):
        self.products = products
        self.prices = prices
        self.qts = qts
        self.index = 0

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1], self.prices[self.index - 1], self.qts[self.index - 1]
        raise StopIteration


order1 = Order()
order1.add_product('banana', 50)
order1.add_product('apple', 40, 2)
order1.add_product('orange', 35, 3)
order1.add_product('bread', 20, 2)

for product, price, qt in order1:
    print(f'{product}: {price} UAH x {qt} item')
