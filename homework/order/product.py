
class Product:
    def __init__(self, name, price, stock, desc):
        self.name = name
        self.price = int(price)
        self.stock = int(stock)
        self.description = desc

    def __str__(self):
        return f'{self.name}, price: {self.price}'
