"""
Вводиться з клавіатури користувачем текст. 
Знайти в ньому найдовше слово та вивести його на екран
"""
text = 'Hello, world! Today is a beautiful day!'

text = text.split()
print(max(text, key=len))

"""
Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери).
Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту.
Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
aaaaaaa - Вовочка писав слово - "a"
ititititit - Вовочка писав слово - "it"
catcatcatcat - Вовочка писав слово - "cat"
"""

text = 'olgaolgaolgaolga'

for i in range(1, len(text) // 2 + 1):
    pattern = text[:i]
    if len(pattern) * text.count(pattern) == len(text):
        print(pattern)
        break

# Define the execution time for script running

stp = """
text = input('text = ')
"""

import timeit

s = """
for i in range(1, len(text) // 2 + 1):
    pattern = text[:i]
    if len(pattern) * text.count(pattern) == len(text):
        print(pattern)
        break
"""
print(timeit.timeit(s, setup=stp, number=1000))
