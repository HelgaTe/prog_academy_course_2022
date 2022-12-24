import datetime
from dateutil import relativedelta
import logging


logger = logging.Logger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler = logging.FileHandler(f'add_student.log')
handler.setFormatter(formatter)
logger.addHandler(handler)
class GroupLimitError(Exception):
    def __init__(self, limit):
        self.limit = limit

    def __str__(self):
        return f'Group limit of {self.limit} students is reached'


class UniqStudentError(Exception):
    def __init__(self, student, course):
        self.student = student
        self.title = course

    def __str__(self):
        return f'{self.student} is already added into group {self.title}'


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

    def __init__(self, course: str, limit: int = 10):
        if not isinstance(limit, int):
            raise TypeError
        if limit < 0:
            raise ValueError
        self.course = course
        self.limit = limit
        self.students = []

    def add_student(self, student: Student):
        if student in self.students:
            raise UniqStudentError(student, self.course)
        if len(self.students) >= self.limit:
            raise GroupLimitError(self.limit)
        self.students.append(student)
        logger.info(f'{self.course}, {student}')
        return self.students

    def remove_student(self, student: Student):
        if student in self.students:
            self.students.remove(student)

    def __str__(self):
        return f'{self.course} group:\n' + '\n'.join(map(str, self.students))




if __name__ == '__main__':
    try:
        student1 = Student('Olha', 'Telizhuk', 'Kyiv', 1991, 1, 15)
        group1 = Group('PYTHON', limit=10)

        group1.add_student(student1)
        group1.add_student(Student('David', 'Davidov', 'Lviv', 1992, 5, 19))
        group1.add_student(Student('Ivan', 'Baran', 'Kyiv', 1990, 12, 7))
        group1.add_student(Student('Misha', 'Mishka', 'Kharkiv', 1993, 8, 18))
        # group1.add_student(student1)
        print(group1)
    except Exception as error:
        print(error)

