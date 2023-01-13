from dataclasses import dataclass


@dataclass
class Students:
    name: str
    surname: str


class Group:
    def __init__(self, course, limit=10):
        self.course = course
        self.limit = limit
        self.students = []

    def add_to_group(self, student):
        self.students.append(student)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.students[item]
        raise TypeError

    def __iter__(self):
        index = 0
        while index < len(self.students):
            yield self.students[index]
            index += 1

    def __str__(self):
        return '\n'.join(map(str, self.students))


if __name__ == '__main__':
    x1 = Students('Ivan', 'Ivanov')
    x2 = Students('Ivan', 'Ivanov')
    x3 = Students('Ivan3', 'Ivanov')
    x4 = Students('Ivan4', 'Ivanov')
    x5 = Students('Ivan5', 'Ivanov')
    print(x1)
    print(x1 == x2)

    group = Group('Python')
    group.add_to_group(x1)
    group.add_to_group(x2)
    group.add_to_group(x3)
    group.add_to_group(x4)
    group.add_to_group(x5)
    for i in group:
        print(f'Iterator works: {i}')

    print(f'GetItem works: {group[-1]}')
