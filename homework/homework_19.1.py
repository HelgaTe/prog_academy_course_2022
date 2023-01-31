"""
Task 1: Создайте декоратор, который зарегистрирует декорируемый класс в списке классов.
"""

class ClassDecorator:
    list_of_cls = []
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if self.cls not in ClassDecorator.list_of_cls:
            ClassDecorator.list_of_cls.append(self.cls)
        return self.cls(*args, **kwargs)
@ClassDecorator
class Test1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

@ClassDecorator
class Test2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ == '__main__':

    t1 = Test1(10, 10)
    t2 = Test2(12, 18)

    print(Test1.list_of_cls)
    print(Test2.list_of_cls)