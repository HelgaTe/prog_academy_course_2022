"""
Task 1: Реалізуйте генераторну функцію, яка повертатиме по одному члену
геометричної прогресії із зазначеним множником. Генератор повинен зупинити свою роботу
або після досягнення зазначеного елементу, або при передачі команди на завершення
"""


def geometric_prog(start, q):
    while True:
        yield start
        start *= q


obj = geometric_prog(3, 5)  # generator object

for i in obj:
    print(i)
    if i > 1_000_000:
        obj.close()

print('=' * 40)
"""
Task 2:Реалізуйте свій аналог генераторної функції range().
"""


def my_range(*args):
    start, stop, step = 0, None, 1
    if len(args) == 1:
        stop = args
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError

    if not isinstance(start, int):
        raise TypeError
    if not isinstance(stop, int):
        raise TypeError
    if not isinstance(step, int):
        raise TypeError

    if not step:
        raise ValueError
    if step < 0 and stop > start:
        return
    if step > 0 and stop < start:
        return
    while abs(start) < abs(stop):
        yield start
        start += step


# print(*my_range(20))
print(*my_range(10, 20, 5))
print(*my_range(-10, 20, 5))
print(*my_range(-10, -20, 5))
print(*my_range(-10, -20, -5))
print(*my_range(10, -20, 5))
print(*my_range(10, 20, -5))
print(*my_range(10, -20, -5))

print('=' * 40)
"""
Task 3: Напишіть функцію-генератор, яка повертатиме прості числа. 
Верхня межа діапазону повинна бути задана параметром цієї функції.
"""


def prime_num(stop: int):
    for n in range(2, stop + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n


for i in prime_num(100):
    print(i)

print('=' * 40)
"""
Task 4: Напишіть генераторний вираз для заповнення списку. 
Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.
"""

x = (item * item * item for item in range (2, 10))
print(*x)


