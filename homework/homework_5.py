'''
Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
Примітка: щасливим квитком називається число, у якому, при парній кількості цифр,
сума цифр його лівої половини дорівнює сумі цифр його правої половини.
Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.
'''

numbers = input('numbers = ')

sum_begin = numbers[0:2]
sum_end = numbers[2:4]
a, b = int(sum_begin[0]), int(sum_begin[1])
c, d = int(sum_end[0]), int(sum_end[1])

res = 'lucky ticket' if a + b == c + d else 'simple ticket'
print(res)

# Alternative
ticket_num = input('Ticket number: ')
if len(ticket_num) % 2:
    print('input error')
else:
    ticket_num = list(map(int, ticket_num))
    mid = len(ticket_num) // 2
    res = 'lucky ticket' if sum(ticket_num[:mid]) == sum(ticket_num[mid::]) else 'simple ticket'
    print(res)


'''
З клавіатури вводиться число (шестизначне). Перевірити, чи воно є паліндромом.
Примітка: Паліндром називається число, слово або текст, які однаково читаються
зліва направо і справа наліво.
Наприклад, це числа 143341, 5555, 7117 і т.д.
'''

number = input('number = ')

part1 = number[0:3]
part2 = number[::-1][0:3]

res = 'Yes' if part1 == part2 else 'No'
print(res)

# Alternative
num = input('number: ')
rev_num = num[::-1]
result = 'Y' if num == rev_num else 'N'
print(result)


"""
Дано коло з центром на початку координат та радіусом 4.
Користувач вводить з клавіатури координати точки x та y.
Написати програму, яка визначить, лежить ця точка всередині кола чи ні
"""

# x2 + y2 = R2

x, y = int(input('x = ')), int(input('y = '))
r = 4
if x**2 + y**2 == r**2:
    print('(x,y) is on the cycle')
elif x**2 + y**2 < r**2:
    print('(x,y) is in the cycle')
else:
    print('(x,y) is out of the cycle')