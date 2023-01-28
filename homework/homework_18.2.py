"""
Task2:
Создайте декоратор, который зарегистрирует декорируемую функцию в
списке функций, для обработки последовательности.
"""

list_of_funcs = []
def add_func(f): # callable obj, that will be used as decorator
    list_of_funcs.append(f)
    return f

@add_func
def suma(a, b):
    return  a + b
@add_func
def mul(a, b):
    return a * b

@add_func
def sub(a, b):
    return a - b
@add_func
def expon(a, b):
    return a**b


print(f'List of registered functions: {list_of_funcs}')

a, b = 20, 4
for i in list_of_funcs:
    res = i(a, b)
    print(f'Function {i.__name__}>: {res}')
