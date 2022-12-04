"""
Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
Виведіть значення цього паліндрому і те, vyj;tyyzv яких чисел він є
"""


def three_digit_num():
    palindrome_list = []
    for i in range(100, 1_000):
        for j in range(100, 1_000):
            res = str(i * j)
            mid = len(res) // 2
            a = res[:mid]
            b = res[mid::]
            if a == b[::-1]:
                palindrome_list.append(f'{i} x {j} = {res}')
    return palindrome_list[-1]


print(three_digit_num())


def two_digit_num():
    palindrome_list = []
    for i in range(10, 100):
        for j in range(10, 100):
            res = str(i * j)
            mid = len(res) // 2
            a = res[:mid]
            b = res[mid::]
            if a == b[::-1]:
                palindrome_list.append(f'{i} x {j} = {res}')
    return palindrome_list[-1]


print(two_digit_num())
