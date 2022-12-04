"""
FUNCTIONS
- decomposition (resample task into smaller parts)
- code reuse
- make code readable
- name space (LEBG rule : Local -> Enclosing -> Global -> Built-in)
- to simplify code testing

syntax:
def name_func <identifier (a-zA-Z0-9)> (parameters)
...
    return

layers in app development (minimal set):
    - data -> logic -> UserInterface -> communication
"""


def suma(a, b):
    return a + b


print(suma(12, 23))
print(suma('12', '23'))


def f_out(): # LEBG rule review
    sum = 20
    a = 20

    def f_in():
        a = 30
        return sum + a

    return f_in() ** 2


print(f_out())

def func(seq):
    for index, item in enumerate(seq):
        seq[index] *= 2
    return seq


x = [1, 2, 3, 4, 5]  # list is mutable object
y = [1, 2, 3, 4, 5]  # list is mutable object
res1 = func(x[:])  # apply func to copy of <x> to avoid changing initial value of <x>
res2 = func(y)  # apply func and modify initial <y> value
print(y)
print(res2)
print('=' * 20)
print(x)
print(res1)

# Parameters & arguments

def func(*agrs, **kwargs):
    print(agrs)
    print(kwargs)
    return sum(agrs)


print(func(1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 5, 6, 3, a='hello', b='python'))

