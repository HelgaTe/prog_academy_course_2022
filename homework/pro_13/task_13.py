"""
Task 1: Создайте ABC класс с абстрактным методом проверки целого числа на
простоту. Т.е., если параметром этого метода является целое число и оно
простое, то метод должен вернуть True, а в противном случае False.
"""
from abc import ABC, abstractmethod
import sympy #  command <pip install sympy>

class AbstractValidator(ABC):
    @abstractmethod # decorator indicates that the method needs to be implemented
    def validate_int(self):
        ...
    @abstractmethod
    def validate_prime(self):
        ...
"""
Task 2: Создайте класс его наследующий
"""
class NumValidator(AbstractValidator):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'Received number: {self.num}'

    def validate_int(self):
        if not self.num % 1:
            return True
        else:
            return False

    def validate_prime(self):
        if sympy.isprime(self.num):
            return True
        else:
            return False
"""
Task 3: Создайте класс, который не наследует пользовательский ABC класс, но
обладает нужным методом. Зарегистрируйте его в качестве виртуального подкласса
"""

class TextValidator:

    def __init__(self, str_line):
        self.str_line = str_line

    def __str__(self):
        return f'Separate validator: {self.str_line}'

    def name_validator(self):
        if self.str_line.isalpha() and self.str_line.istitle():
            return True
        else:
            return False

AbstractValidator.register(TextValidator) # registration


if __name__=='__main__':
    a = NumValidator(12)
    print(a)
    print(a.validate_int(), a.validate_prime(), sep='\n')

    b = TextValidator('olga')
    c = TextValidator('Olga')
    print(b, c, sep='\n')
    print(b.name_validator(), c.name_validator(), sep='\n')

    print(f'{c.__class__} is registered to: {isinstance(c, AbstractValidator)}') # True




