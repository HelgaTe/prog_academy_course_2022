"""
Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці.
На одному поверсі - 4 квартири. Напишіть програму, яка від користувача отримує номер квартири
та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі.
Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це.
"""

from math import ceil

# inputs
floors_per_entrance = 9
flats_per_floor = 4
flats_building = floors_per_entrance * flats_per_floor

flat = int(input('Flat number = '))

if flat > 144:
    print('The flat number is invalid')
else:
    if not int(flat % flats_building):
        section = int(flat // flats_building)
    else:
        section = int(flat // flats_building + 1)
    print(f'Entrance number: {section}')

    if section != 1:
        floor = (flat - (section - 1) * flats_building) / flats_per_floor
        floor = ceil(floor)
        num = ceil((flat - (section - 1) * flats_building) % flats_per_floor)
        if not num:
            num = 4
    else:
        floor = ceil(flat / flats_per_floor)
        num = flat % 4
        if not num:
            num = 4
    print(f'Floor: {floor}')
    print(f'Flat number on the floor: {num}')

# version 2

FLATS_IN_FLOORS = 4
FLOORS = 9
ENTRANCE = 4


# flat = int(input('Flat number = '))
#
# entrance = (flat - 1) // (FLOORS * FLATS_IN_FLOORS) + 1
# floor = (flat - 1) // FLATS_IN_FLOORS - (entrance - 1) * FLOORS + 1
# num_in_floor = (flat - 1) % FLATS_IN_FLOORS + 1
# print(1 <= flat <= FLATS_IN_FLOORS * ENTRANCE and
#       (flat, entrance, floor,num_in_floor) or 'Error')


def get_number(flat_num):
    entrance = (flat_num - 1) // (FLOORS * FLATS_IN_FLOORS) + 1
    floor = (flat_num - 1) // FLATS_IN_FLOORS - (entrance - 1) * FLOORS + 1
    num_in_floor = (flat_num - 1) % FLATS_IN_FLOORS + 1
    return entrance, floor, num_in_floor


while True:
    flat = int(input('Flat number = '))
    if 1 <= flat <= FLATS_IN_FLOORS * FLOORS * ENTRANCE:
        print(*get_number(flat))
        break
    else:
        print('Invalid number')

"""
Написати програму, яка буде повертати для заданого року кількість днів
Рік є високосним, якщо:
    1. рік кратний 400
    2. рік кратний 4 і при цьому не кратний 100
"""
year = int(input("Year = "))

result = f'Number of days in {year}: 366' if not year % 4 and year % 100 or not year % 400 \
    else f'Number of days in {year}: 365'

print(result)

"""
Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої.
Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує такий трикутник
"""

a, b, c = input('a='), input('b='), input('c=')

if a + b > c or b + c > a or c + a > b:
    print('The triangle exists')
else:
    print('The triangle does not exist')
