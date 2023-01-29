# actions applicable to attributes: get, set, delete;
class Students:

    def __init__(self, name, surname, passport):
        self.name = name
        self.surname = surname
        self.__passport = passport
    @property # enable access control
    def passport(self):
        return f'UA {self.__passport}'
    @passport.setter
    def passport(self, value):
        if not isinstance(value, str):
            raise TypeError
        if len(value.strip()) != 6:
            raise ValueError
        self.__passport = value
    @passport.deleter
    def passport(self):
        ...

    def __str__(self):
        return f'{self.surname} {self.name} {self.passport}'


student1 = Students('Inav', 'Ivanov', '12345678')

print(student1.passport)
student1.passport = '123321'
print(student1.passport)

del student1.passport #doesn't work as deleter is set
