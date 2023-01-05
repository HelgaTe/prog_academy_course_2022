class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Student(Human):

    def __init__(self, surname, name, age):
        super().__init__(surname, name)
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, {self.age}'


class Group:

    def __init__(self, title, max_students=10):
        self.title = title
        self.__students = []
        self.max_students = max_students

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError('Student is expected to be instance of class Student')
        if len(self.__students) >= self.max_students:
            raise ValueError('Max student number in group is reached')
        if student in self.__students:
            raise ValueError('The student already exists')
        self.__students.append(student)

        # w/o Raise Exception
        # if student not in self.__students and \
        #         len(self.__students) < self.max_students:
        #     self.__students.append(student)

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)

    def search_student(self, surname):
        search_res = []
        for student in self.__students:
            if student.surname == surname:
                search_res.append(student)
        return search_res

    def __str__(self):
        return f'{self.title} group:\n\n' + '\n'.join(map(str, self.__students))


x = Group('Python', max_students=3)
try:
    x.add_student(Student('Ivan', 'Ivanov', 20))
    x.add_student(Student('Petro', 'Ivanov', 20))
    x.add_student(Student('Petro', 'Petrov', 22))
    x.add_student(Student('Misha', 'Mishka', 21))
except:
    pass

result = x.search_student('Ivanov')
for i in result:
    print(i)
print('=' * 50)
print(x)
