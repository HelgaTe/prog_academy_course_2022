import logger
import exceptions
import student


class Group:

    def __init__(self, course: str, limit: int = 10):
        if not isinstance(limit, int):
            raise TypeError
        if limit < 0:
            raise ValueError
        self.course = course
        self.limit = limit
        self.students = []

    def add_student(self, student: student.Student):
        if student in self.students:
            raise exceptions.UniqStudentError(student, self.course)
        if len(self.students) >= self.limit:
            raise exceptions.GroupLimitError(self.limit)
        self.students.append(student)
        logger.logger.info(f'{self.course}, {student}')
        return self.students

    def remove_student(self, student: student.Student):
        if student in self.students:
            self.students.remove(student)

    def __str__(self):
        return f'{self.course} group:\n' + '\n'.join(map(str, self.students))

    def __iter__(self):
        return StudentIter(self.students)


class StudentIter:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            self.index += 1
            return self.students[self.index - 1]
        raise StopIteration


if __name__ == '__main__':
    try:
        group1 = Group('PYTHON', limit=10)

        group1.add_student(student.Student('Ira', 'Ivanova', 'Lviv', 1991, 5, 19))
        group1.add_student(student.Student('Dima', 'Bondar', 'Kyiv', 1992, 12, 7))
        group1.add_student(student.Student('Mira', 'Koval', 'Kharkiv', 1993, 8, 18))
        group1.add_student(student.Student('David', 'Drizd', 'Odesa', 1989, 1, 13))
        # print(group1)
    except Exception as error:
        print(error)

index = 0
for student in group1:  # Iteration protokol
    index += 1
    # print(index, student.city, student.l_name, student.f_name, student.age)
    print(index, student)