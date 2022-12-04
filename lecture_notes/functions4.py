import operator

x = [1, 2, 3, 4]
print(sum(x))

y = sum  # змінну пов'язати з функцією
print(y(x))


def get_operator(x: str):  # функцію повернути з іншої функції
    if x == '+':
        return operator.add
    if x == '-':
        return operator.sub


print(get_operator('+')(2, 3))
print(get_operator('-')(10, 3))


# version 1
# def filter_items(x, func):  # передати функцію в іншу функцію як агрумент
#     res = [item for item in x if not item % 2]
#     return res

# y = [1, 2, 3, 4, 5, 6, 7]
# print(filter_items(y))

# version 2
def filter_items(x, func):
    res = [item for item in x if func(item)]
    return res


def negative(item):
    return item < 0


def positive(item):
    return item > 0


def even(item):
    return not item % 2


def odd(item):
    return item % 2


def is_5(item):
    return not item % 5


y = [0, 2, 15, -2, 30, -30, 0, 4, -5, 6, 7, 10, -10, -8]
print(filter_items(y, negative))
print(filter_items(y, positive))
print(filter_items(y, even))
print(filter_items(y, odd))
print(filter_items(y, is_5))
print(filter_items(y, lambda item: not item % 3 and not item % 5))
print(filter_items(y, lambda item : item and 'Error')) # use logical operators to add conditions into lambda func





