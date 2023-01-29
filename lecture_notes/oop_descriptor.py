import uuid
class MyDescriptor:
    def __init__(self, attr_name):
        self.attr_name = attr_name
        pass

    def __get__(self, instance, owner):
        if not instance.__dict__.get(self.attr_name):
            instance.__dict__[self.attr_name] = uuid.uuid4()
        return instance.__dict__.get(self.attr_name)

    def __set__(self, instance, value):
        pass

    def __del__(self):
        pass

class Students:
    def __init__(self, name, surname, passport):
        self.name = name
        self.surname = surname
        self.passport = passport

    id = MyDescriptor('id')


st1 = Students('Ivan', 'Ivanov', '12345678')
print(st1.id)