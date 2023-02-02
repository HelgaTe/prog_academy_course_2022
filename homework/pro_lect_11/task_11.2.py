"""
Task 2:
Реализуйте функционал, который будет запрещать установку полей класса
любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
попытаться присвоить, например, строку, то должно быть возбужденно
исключение.
"""

class ElementaryMath:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, key, value):
        if isinstance(value, int):
            self.__dict__[key] = value
        else:
            raise TypeError('<int type> is accepted only')

    def __str__(self):
        return f'a = {self.a}, b = {self.b}'
    def suma(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

example = ElementaryMath(20, 4)
print(example)
print(example.suma())
print(example.mul())

ex = ElementaryMath(20.6, 4.3)
print(ex)
print(ex.suma())
print(ex.mul())