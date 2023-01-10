import datetime
from dateutil import relativedelta
import person


class Student(person.Person):
    def __init__(self, f_name, l_name, city, year, month, day):
        super().__init__(f_name, l_name, city, year, month, day)
        self.age = relativedelta.relativedelta(datetime.date.today(), self.b_day).years

    def __str__(self):
        return f'{self.l_name} {self.f_name}; {self.age} years; {self.city}'



