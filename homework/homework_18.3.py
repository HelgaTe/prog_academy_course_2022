"""
Task3:
Предположим, в классе определен метод __str__, который возвращает строку на основании класса.
Создайте такой декоратор для этого метода, чтобы полученная строка сохранялась в
текстовый файл, имя которого совпадает с именем класса, метод которого вы декорировали.
"""

from typing import Callable
import datetime

def str_file_writer(func: Callable):
    """
    Write result of __str__ function to {name_of_function}.txt file.
    :param func: Function.
    :return: Function with arguments.
    """
    def inner(reference, *args, **kwargs):
        name = type(reference).__name__

        with open(f"{name}.txt", 'w') as file:
            reg_time = datetime.datetime.now()
            file.write(f'{func(reference)}, Logging time: {reg_time}')

        return func(reference)

    return inner
class User:
    def __init__(self, name, login, email):
        self.name = name
        self.login = login
        self.email = email


    @str_file_writer
    def __str__(self):
        line =  f'USER: {self.name}, LOGIN; {self.login}, EMAIL: {self.email}'
        return line


user1 = User('Olha', 'user1', 'user1@gmail.com')
print(user1)
print(user1.__class__)
print(type(user1).__name__)



