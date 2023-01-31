"""
Task 2: Создайте декоратор класса с параметром. Параметром должна быть
строка, которая должна дописываться (слева) к результату работы метода __str__.
"""

class AddStr:
    """
    Add text (set as parameter of decorator) to __str__ method of class.
    """
    def __init__(self, text):
        self.text = text

    def __call__(self, func):
        def inner(*args, **kwargs):
            result = self.text + func(*args, **kwargs)
            return result
        return inner

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @AddStr('The result is: ')
    def __str__(self):
        return f'{self.a} x {self.b}'

if __name__ == '__main__':
    a1 = A(10, 30)
    print(a1) # stdout w/o decorator >>> 10 x 30
    print(a1) # stdout w/o decorator >>> # The result is: 10 x 30