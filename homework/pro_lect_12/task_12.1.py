"""
Task 1: Реализуйте метакласс, который обладает следующим функционалом: при
его использовании в файл с заранее определенным названием нужно
сохранить имя класса и список его полей.
"""
import datetime

class MyMeta(type):
    """
    MyMeta class intercepts info about the class being processed and write it to the file
    """
    def __new__(mcs, class_name, bases, attrs): # called out to create class (msc - metaclass)
        return type.__new__(mcs, class_name, bases, attrs)

    def __init__(cls, class_name, bases, attrs): # called out to initialize class (cls - class)
        create_time = datetime.datetime.now().replace(microsecond=0)
        with open ('my_meta_register.txt', 'a') as f:
            f.write(f'class_name: {class_name}; '
                    f'created: {create_time}; '
                    f'inherited from: {bases}; '
                    f'attrs: {attrs.items()}\n')

class A:
    pass
class B(A, metaclass=MyMeta):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Box: {self.a} x {self.b} x {self.c}'

class C(A, metaclass=MyMeta):
    pass


if __name__=='__main__':
    box1 = B(3, 5, 6)
    print(box1)

