import math


class Rational:
    def __init__(self, a: int, b: int):
        if not isinstance(a, int) and not isinstance(b, int):
            raise TypeError(f'Check data type for param a: {type(self.a)} or/and for param b: {type(self.b)}')
        if not b:
            raise ZeroDivisionError
        self.a = a
        self.b = b

    def __str__(self):
        sign = '' if self.a * self.b > 0 else '-'
        a, b = abs(self.a), abs(self.b)
        # method math.gcd() returns the greatest common divisor of the two integers
        c = math.gcd(a, b)  # c - common denominator
        a //= c
        b //= c

        if a == b:
            return f'{sign}1'
        if b == 1:
            return f'{sign}{a}'
        if a > b:
            return f'{sign}{a // b} {a - a // b * b}/{b}'
        return f'{sign}{a}/{b}'

    def __eq__(self, other):
        c = math.gcd(self.a, self.b)
        self.a //= c
        self.b //= c

        c = math.gcd(other.a, other.b)
        other.a //= c
        other.b //= c
        return (self.a, self.b) == (other.a, other.b)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.a / self.b < other.a / other.b

    def __gt__(self, other):
        return self.a / self.b > other.a / other.b

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.a * self.b > 0 else -1
        d = self.b * other.b  # d -denominator
        n = d // self.b * self.a - d // other.b * other.a  # n - numerator
        if not n:
            return 0
        return Rational(sign * n, d)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.a * self.b > 0 else -1
        d = self.b * other.b  # d -denominator
        n = d // other.b * other.a - d // self.b * self.a  # n - numerator
        return Rational(sign * n, d)

    def __isub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.a * self.b > 0 else -1
        d = abs(self.b) * abs(other.b)  # d -denominator
        n = d // abs(self.b) * abs(self.a) - d // abs(other.b) * abs(other.a)  # n - numerator
        self.a = sign * n
        self.b = d
        return self

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.a * self.b else -1
        d = self.b * other.b
        n = d // self.b * self.a + d // other.b * other.a
        return Rational(sign * n, d)

    def __radd__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.a * self.b else -1
        d = self.b * other.b
        n = d // self.b * self.a + d // other.b * other.a
        return Rational(sign * n, d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.a * self.b else -1
        d = self.b * other.b
        n = self.a * other.a
        return Rational(sign * n, d)

    def __rmul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.a * self.b else -1
        d = self.b * other.b
        n = self.a * other.a
        return Rational(sign * n, d)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.a * self.b else -1
        d = self.b * other.a
        n = self.a * other.b
        return Rational(sign * n, d)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.a * self.b else -1
        d = self.b * other.a
        n = self.a * other.b
        return Rational(sign * n, d)


if __name__ == '__main__':
    x = Rational(30, 10)
    y = Rational(5, 10)
    print(x, y, sep='\n')
    print((x != y), (x == y), sep='\n')
    print((x > y), (x < y), sep='\n')

    # y -= x
    # print(y)

    # print(y - 2)
    # print(2 - y)
    # print(y - Rational(1, 2))

    # a = Rational(4, 2)
    # print(-4 - a)

    # a1 = Rational(1, 2)
    # a2 = Rational(2, 4)
    # print(a1 == a2)

    # print(1 + x)
    # print(x + 1)

    # x = Rational(5, 9)
    # y = Rational(3, 10)
    # print(x)
    # print(y)
    # print(x*y)
    # print(3*x)

    # x = Rational(5, 24)
    # y = Rational(15, 16)
    # print(15/y)
    # print(x/5)
