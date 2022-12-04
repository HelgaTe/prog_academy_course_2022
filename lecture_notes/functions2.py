text = input('text = ')
res = {}

for item in text:
    if item.isalpha() and not res.get(item):
        res[item] = text.count(item)
print(res)

import operator


def my_pow(a, b):
    return a ** b


calc = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    '^': my_pow,
}

op = input('operator = ')
a = int(input('a = '))
b = int(input('b = '))

print(calc[op](a, b))

person ={
    'name' : 'Yehor',
    'surname':'Boyko',
    'address': {
        'city': 'Kyiv',
        'street': 'Main',
    }
}

print(person['name'])
print(person['address']['street'])