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
