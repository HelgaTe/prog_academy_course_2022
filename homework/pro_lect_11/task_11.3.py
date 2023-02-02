"""
Task 3: Реализуйте свойство класса, которое обладает следующим
функционалом: при установки значения этого свойства в файл с заранее
определенным названием должно сохранятся время (когда устанавливали
значение свойства) и установленное значение.
"""
import datetime
def set_param_time(func):
    def inner(ref, *args, **kwargs):
        name = type(ref).__name__
        obj = ref.__dict__
        with open(f'{name}_set_param_time.txt', 'a') as file:
            set_time = datetime.datetime.now().replace(microsecond=0)
            line = f'class: {name};set time: {set_time}, set params: {obj}\n'
            file.write(line)
        return func(ref)

    return inner

class User:

    def __init__(self, name, id):
        self.name = name
        self.passport = f'UA-{id}'
    @set_param_time
    def __str__(self):
        return f'{self.name}, {self.passport}'


if __name__=='__main__':
    user1 = User('Olga', '123456')
    user2 = User('Ivan', '234567')
    user3 = User('John', '987654')

    print(user1)
    print(user2)
    print(user3)
