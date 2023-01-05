import datetime
from dateutil import relativedelta


class Person:
    def __init__(self, f_name, l_name, city, year, month, day):
        self.f_name = f_name
        self.l_name = l_name
        self.city = city
        self.b_day = datetime.date(year, month, day)

    def __str__(self):
        return f'{self.l_name} {self.f_name}; {self.b_day}; {self.city}'


class Student(Person):
    def __init__(self, f_name, l_name, city, year, month, day):
        super().__init__(f_name, l_name, city, year, month, day)
        self.age = relativedelta.relativedelta(datetime.date.today(), self.b_day).years

    def __str__(self):
        return f'{self.l_name} {self.f_name}; {self.age} years; {self.city}'


class Group:

    def __init__(self, course, limit=10):
        self.course = course
        self.limit = limit
        self.students = []

    def add_student(self, student):
        if student not in self.students and \
                len(self.students) < self.limit:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def __str__(self):
        return f'{self.course} group:\n' + '\n'.join(map(str, self.students))


if __name__ == '__main__':
    per1 = Person('Olha', 'Telizhuk', 'Kyiv', 1991, 1, 15)

    student1 = Student('Olha', 'Telizhuk', 'Kyiv', 1991, 1, 15)
    student2 = Student('David', 'Davidov', 'Lviv', 1992, 5, 19)
    student3 = Student('Ivan', 'Baran', 'Kyiv', 1990, 12, 7)
    student4 = Student('Ivan', 'Baran', 'Kyiv', 1990, 12, 7)

    group1 = Group('PYTHON')

    group1.add_student(student1)
    group1.add_student(student2)
    group1.add_student(student3)
    group1.add_student(student4)

    print(per1)
    print('=' * 50)
    print(student2)
    print('=' * 50)
    print(group1)
