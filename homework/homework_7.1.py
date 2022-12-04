"""
Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту
"""

text = 'behind black basket'

selection = text.count('b')
print(selection)

"""
Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки
введеного ім'я на валідність (мається на увазі, що, наприклад, в імені людини
не може бути цифр, воно повинно починатися з великої літери, за якою повинні йти маленькі).
"""
name = input('name = ')

if name.isalpha() and name.istitle():
    print('Accepted name')
else:
    print('Error')

"""
Напишіть програму, яка обчислить суму всіх кодів символів рядка
"""

text = input('text = ')
res = sum(text.encode('utf-8'))
print(res)

"""
Виведіть на екран 10 рядків із значенням числа Pi.
У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.
"""
import math

for i in range(2, 12):
    res = f'{math.pi:.{i}f}'
    print(res)

"""
Вводиться з клавіатури користувачем текст.
Знайти в ньому найдовше слово та вивести його на екран
"""
text = input('text = ')
# text ='Hello, world! Today is a beautiful day!'

new = []
for t in text.split():
    new.append([int(len(t)), t])
    selection = sorted(new)[-1]
print(f'The largest word: {selection[-1]}')
