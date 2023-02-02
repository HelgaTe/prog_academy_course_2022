"""
Task 1: Создайте дескриптор, который будет делать поля класса управляемые им
доступными только для чтения.
"""

class MyDescriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        raise AttributeError('The field is read-only')

    def __delete__(self, instance):
        ...


class User:
    country = MyDescriptor('Ukraine')

    def __init__(self, name, id):
        self.name = name
        self.passport = f'UA-{id}'

    def __str__(self):
        return f'{self.country} | {self.name}, {self.passport}'

user1 = User('Olga', '123456')
print(user1)
user1.country = 'Canada'
