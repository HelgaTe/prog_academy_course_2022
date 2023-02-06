"""
Task 1: Создайте дескриптор, который будет делать поля класса управляемые им
доступными только для чтения.
"""

class MyDescriptor:

    def __init__(self, attr_name):
        self.attr = attr_name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.attr)
    def __set__(self, instance, value):
        if self.attr not in instance.__dict__:
            instance.__dict__[self.attr] = value
        else:
            raise AttributeError('The field is read-only')

    def __delete__(self, instance):
        raise AttributeError('The field is read-only')


class User:
    country = MyDescriptor('country')

    def __init__(self, name, id, country = "Ukraine"):
        self.name = name
        self.passport = f'UA-{id}'
        self.country = country


    def __str__(self):
        return f'{self.name}, {self.passport} | {self.country}'

user1 = User('Olga', '123456')
user2 = User('Ivan', '789078',country='USA')
print(user1, user2, sep='\n')
user1.country = 'Canada'
