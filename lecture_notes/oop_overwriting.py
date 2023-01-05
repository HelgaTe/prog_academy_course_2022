from decimal import Decimal
import random

print(0.1 + 0.1 + 0.1 == 0.3)  # don't compare float numbers - it will return False
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3'))  # to avoid failure - use decimal
print('=' * 50)


class Box:

    def __init__(self, x: (int, float), y: (int, float), z: (int, float)):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __lt__(self, other):  # code convention requires to overwrite inversion method
        return self.volume() < other.volume()

    def __add__(self, other):
        if isinstance(other, Box):
            return self.volume() + other.volume()
        if isinstance(other, (int, float)):
            return self.volume() + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.volume() + other
        return NotImplemented

    def __str__(self):
        return f'{self.x} x {self.y} x {self.z}'


def box_suma(list_of_boxes):
    s = 0
    for item in list_of_boxes:
        s = s + item
    return s


a = Box(2, 5, 10)
b = Box(1, 5, 2)
print(a)
print(b)
print(a < b)

print(a.__gt__(b))
print('\n'.join(dir(object)))  # show all method attributed to object
print('=' * 50)
boxes = [Box(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)) for i in range(1, 10)]
boxes.sort()
print('\n'.join(map(str, boxes))+'\n')

print(f'sum of boxes volume: {box_suma(boxes)}')
print(f'the larges box: {max(boxes)}')
print(f'the smallest box: {min(boxes)}')

