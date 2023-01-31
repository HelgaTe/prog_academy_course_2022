"""
Task 3:
Для класса Box напишите статический метод, который будет подсчитывать
суммарный объем двух ящиков, которые будут его параметрами.

"""


class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'{self.a} x {self.b} x {self.c}'

    def volume(self):
        return self.a * self.b * self.c
    @staticmethod
    def total_volume(x, y):
        if isinstance(x, Box) and isinstance(y, Box):
            return x.volume() + y.volume()


if __name__=='__main__':
    box1 = Box(5, 6, 6)
    box2 = Box(10, 4, 2)
    print(f'Volume: {box1.volume()}')
    print(f'Str method: {box1}')

    print(f'Staticmethod: {Box.total_volume(box1, box2)}')