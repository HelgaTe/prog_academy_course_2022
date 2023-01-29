# methods to control attributes: get attr, set attr, del attr, get attribute
class Students:
    __attrs= ('surname', 'name', 'passport','age', 'b_day', 'nationality')
    def __init__(self, name, surname, passport):
        self.name = name
        self.surname = surname
        self.passport = passport


    # def __getattr__(self, item):
    #     if item in Students.__attrs:
    #         self.__dict__[item] = None
    #         return self.__dict__[item]
    #     else:
    #         raise AttributeError
    #     # return f'<{item}> is absent'

    def __getattribute__(self, item): #
        try:
            return object.__getattribute__(self,item)
        except AttributeError:
            if item in Students.__attrs:
                self.__dict__[item] = None
                return self.__dict__[item]

    def __setattr__(self, key, value):
        if key in Students.__attrs:
            if key == 'nationality' and value.lower() == 'russian':
                raise ValueError('No such nationality exists. Russian warship, go fuck yourself!')
            self.__dict__[key] = value
        else:
            raise AttributeError
    def __delattr__(self, item):
        if item in ['surname', 'name', 'passport']:
            ...
        else:
            del self.__dict__[item]

    def __str__(self):
        return '; '.join(map(lambda item: f'<{item[0]}>: {item[1]}', self.__dict__.items()))


student1 = Students('Inav', 'Ivanov', '12345678')

student1.age = 20
student1.nationality = 'Ukrainian'
print(student1.age)
print(student1.nationality)
# student1.nationality = 'russian'
# print(student1.nationality)
print(student1)
del student1.surname
del student1.age
print(student1)
