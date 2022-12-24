import datetime


class Person:
    def __init__(self, f_name, l_name, city, year, month, day):
        self.f_name = f_name
        self.l_name = l_name
        self.city = city
        self.b_day = datetime.date(year, month, day)

    def __str__(self):
        return f'{self.l_name} {self.f_name}; {self.b_day}; {self.city}'
