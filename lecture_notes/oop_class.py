class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}.'


class Group():
    def __init__(self, title):
        self.title = title
        self.student = []

    def add_student(self, student):
        if student not in self.student:
            self.student.append(student)

    def __str__(self):
        return f"{self.title}\n{'-'*10}\n" + '\n'.join(map(str, self.student)) + '\n'



student_1 = Student('Ivan', 'Ivanov')
student_2 = Student('Petro', 'Petrov')
student_3 = Student('Olha', 'Telizhuk')

group_python = Group('Python IT Gen')
group_python.add_student(student_1)
group_python.add_student(student_2)
group_python.add_student(student_3)

group_eng = Group('Business English')
group_eng.add_student(student_1)
group_eng.add_student(student_2)

print(group_eng)
print(group_python)
