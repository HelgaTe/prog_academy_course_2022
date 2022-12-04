"""
Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером
"""
day = input('day of week = ')

week = {
    '1': 'Monday',
    '2': 'Tuesday',
    '3': ' Wednesday',
    '4': 'Thursday',
    '5': 'Friday',
    '6': 'Saturday',
    '7': 'Sunday'
}
# we shall verify data put by users and handle incorrect data to avoid code failure
print(week.get(day,'Error'))

"""
Опишіть кота (домашня тварина) на основі словника
"""
my_cat = {
    'breed': 'abyssinian',
    'size': 'medium',
    'age': '3 years',
    'coat': 'short, fine, silky',
    'color': 'blue'
}

print(my_cat.get('breed'))

"""
Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику, скільки разів яка літера зустрічається в цьому рядку
"""
text = input('text = ')

# version 1 (only letters are accounted, no whitespaces or punctuation)
stat = {}
word = str(text.split())
for item in word:
    if item.isalpha():
        stat[item] = word.count(item)
print(f'version 1 {stat}')

# version 2 - use <set data type> (whitespaces and punctuation are accounted)
for i in set(text):
    stat[i] = text.count(i)
print(f'version 2 {stat}')

# version 3 - use <dictionary comprehension> (leave out whitespaces and punctuation)

res = {item: text.count(item) for item in set(text) if item.isalpha()}
print(f'version 3 {res}')

# version 4 - use <lambda>
out = '\n'.join(map(lambda item : f'{item[0]}, {item[1]}', res.items()))
print(out)


"""
Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери, які є одночасно і в першому, і в другому рядку.
"""
t1 = set(input('text_1 = '))
t2 = set(input('text_2 = '))

print(t1 & t2)

"""
Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5
"""

num_1 = list(range(3, 100, 3))
num_2 = list(range(5, 100, 5))
out = set(num_1) & set(num_2)
print(out)

"""
Створіть список із числами, які є в обох списках
"""

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [3, 5, 6, 8, 9, 0]

res = set(l1) | set(l2)
print(res)
