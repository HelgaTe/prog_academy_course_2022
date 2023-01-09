class Rectangle:
    def __init__(self, a, b):
        if not a or not b:
            raise ValueError('Null is not accepted')
        elif a < 0 or b < 0:
            raise ValueError('Negative numbers are not accepted')
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.a = a
            self.b = b

    def __str__(self):
        return f'{self.a} x {self.b}'

    def __gt__(self, other):
        return self.square > other.square

    def __lt__(self, other):
        return self.square < other.square

    def square(self):
        s = self.a * self.b
        return s

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.square() + other.square()
        if isinstance(other, (int, float)):
            return self.square() + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.square() + other
        return NotImplemented

    def __mul__(self, other):
        if not other:
            raise ValueError('Null in not accepted')
        elif other < 0:
            raise ValueError('Negative numbers are not accepted')
        elif isinstance(other, (int, float)):
            return self.square() * other
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.square() * other
        return NotImplemented


if __name__ == '__main__':
    x = Rectangle(10, 10)
    y = Rectangle(10, 8)
    a = x + y
    print(x.square() > y.square())
    print(a)
    print(x + Rectangle(1, 1))
    print(x + 12)
    print(12 + x)
    print(10 * x)
    print(x * 10)
