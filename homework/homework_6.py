"""
1. Написати Python-скрипт, який виводить на екран усі числа в діапазоні від 1 до 100 кратні 7
"""
w = [i for i in range(101) if not i % 7]
print(w)

# better way
y = [i for i in range(7,101,7) if not i % 7] # set step <7> to make less iterations
print(y)

"""
2. Написати Python-скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури).
"""

n = int(input('n = '))

result = 1
for num in range(1, n+1):
    result *= num
    print(result)

"""
3. Написати Python-скрипт, який виводить на екран таблицю множення на 5.
Переважно друкувати 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10,
"""
# num = int(input('num = '))

# print(f'Таблиця множення на {num}')
# for item in range(1,11):
#     value = item * num
#     print(item, 'x', num, '=', value)

for i in range(1,11):
    for j in range(1,11):
        print(f'{i} x {j} = {i * j}')
    print('*'*20)

"""
4. Написати Python-скрипт, який виводить на екран прямокутник із '*'.
Висота і ширина прямокутника вводяться з клавіатури.
Наприклад, нижче представлений прямокутник з висотою 4 та шириною 5
"""

h = int(input('h='))
w = int(input('w='))

print('*' * w)
for i in range(h - 2):
    print('*', ' ' * (w - 4), '*')
# print('*' * w)


# n, m = int(input('n=')), int(input('m='))
#
# res = f"{'*' * m}\n" + f"*{' ' * (m-2)}*\n"*(n-2) + f"{'*' * m}\n"
# print(res)

"""
5. Є список [0,5,2,4,7,1,3,19]. Написати Python-скрипт для підрахунку непарних цифр у ньому
"""

in_list = [0, 5, 2, 4, 7, 1, 3, 19]
# step by step code
new_list = [i for i in in_list if i % 2]
odd_quantity = len(new_list)
print(new_list)
print(odd_quantity)

# one line code
result = len([i for i in in_list if i % 2])
print(result)


# homework review

x= [1,2,3,4,5,6]
count = 0
for item in x:
    if item % 2:
        count +=1
print(count)

"""
6. Створіть список випадкових чисел (розміром 4 елементи). Створіть другий список у два рази більше першого,
де перші 4 елементи повинні дорівнювати елементам першого списку, а решта елементів - подвоєним значенням початкових.
    Було → [1,4,7,2]
    Стало → [1,4,7,2,2,8,14,4]
"""

import random
#
# list1 = [random.randint(1, 9) for i in range(4)]
# list2 = [item*2 for item in list1]
# result = list1 + list2
#
# print(list1)
# print(list2)
# print('='*26)
# print(result)


# homework review
x = [random.randint(1,100) for _ in range(4)]
print(x)
y = x[:] + [item + item for item in x]
print(y)


"""
7. Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць.
Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.
"""

import random

salary_list = [random.randint(1,60000) for _ in range(25)]  # salary for the last two years
avg = round(sum(salary_list[-12:])/12)

print(salary_list)
print(avg)

"""
8. 
    [1, 2, 3, 4]
    [5, 6, 7, 8]
    [9,10, 11, 12]
    [13,14, 15, 16]
Напишіть Python-скрипт, який виведе цю матрицю на екран,
обчислить та виведе суму елементів цієї матриці.
"""

x = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10, 11, 12],
    [13,14, 15, 16]
    ]

for row in x:
    matrix = '\t'.join(map(str,row))
    print(matrix)

lev1 = []
for i in x:
    lev1.append(sum(i))
res = sum(lev1)

print('Sum of matrix element:',res)


"""
9. Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
Список може бути довільною довжиною.
"""

a = [7, 2, 9, 4]

b = list(reversed(a)) # create new list
print(b)

for i in reversed(a): # not creating new list, just iterating through the elements
    print(i)

"""
10. За допомогою циклів вивести на екран усі прості числа від 1 до 100.
    *Просте число  — натуральне число, яке має рівно два різних натуральних дільники (лише 1 і саме число).
    *Послідовність простих чисел до 100:
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
"""

for n in range(1, 101):
    for i in range(2, n):
        if not n % i:
            break
    else:
        print(n)

"""
11. Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується з клавіатури (число непарне).
У прикладі ширина дорівнює 5.
*****
 ***
  *
 ***
*****
"""
num = int(input('num='))
num_list = [i for i in range(1, num+1) if i% 2]
new = list(reversed(num_list))+num_list[1::]
print(new)

for n in new:
    print((n*'*').center(num))





