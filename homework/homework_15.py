class Order:
    def __init__(self):
        self.products = []
        self.quantities = []
        self.prices = []

    def add_product(self, product, price, qt=1):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += qt
        else:
            self.products.append(product)
            self.prices.append(price)
            self.quantities.append(qt)

    def amount(self):
        amount = 0
        for index, item in enumerate(self.products):
            amount += item.price * self.quantities[index]
        return amount

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

    def __len__(self):
        return self.index

    def __getitem__(self, item):
        if isinstance(item, int):
            if item > self.index:
                raise IndexError
            return item
        if isinstance(item, slice):
            output = []
            start = item.start or 0
            stop = item.stop or self.index + 1
            step = item.step or 1
            for i in range(start, stop, step):
                output.append(i)
            return result
        raise TypeError


if __name__ == '__main__':
    order1 = Order()
    order1.add_product('banana', 60)
    order1.add_product('apple', 20, 2)
    order1.add_product('orange', 70, 3)
    order1.add_product('kiwi', 90)

    # Iteration protokol
    num = 1
    for product, price, qt in order1:
        num += 1
        print(f'{num}. {product}:  {price} UAH x {qt} item. Total {price * qt} UAH')
    print('='*50)

    # Sequence protokol
    result = list(order1)
    print(f'Number of products in order: {len(result)}')
    print(result[:])
    print(result[2])
    print(result[1:3])
