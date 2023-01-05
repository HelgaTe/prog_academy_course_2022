class BaseA:
    def __init__(self):
        self.a = 10

    def method(self):
        return self.a


class SubB(BaseA):
    def __init__(self):
        super().__init__()
        self.b = 20

    def sub_method(self):
        return self.b

    def method(self):
        return super().method() + self.b


x = SubB()
print(x.method())
print('=' * 50)
print(SubB.__dict__.keys())
print(x.__dict__)
print('=' * 50)
print(SubB.__mro__)
