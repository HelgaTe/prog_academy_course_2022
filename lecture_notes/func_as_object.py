# 1 - function as a variable
x = sum
print(x([10, 15, 6]))
print(sum([10, 15, 6]))

# 2 - function as an argument

def selection(a, func):
    for item in a:
        if func(item):
            yield item

import random
y = [random.randint(-20, 20) for _ in range(20)]
for i in selection(y, lambda i: i < 0):
    print(f'Selected item < 0: {i}')

# 3 - function as value returned by other function
import operator
def calc(op):
    if op == '+':
        return operator.add
    if op == '-':
        return operator.sub

n, m = int(input('a= ')), int(input('b= '))
op = input('operator= ')

print(calc(op)(n, m))