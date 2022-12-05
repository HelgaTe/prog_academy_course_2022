"""
Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
Наприклад: XXII -> 22
"""
rom_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

roman_num = 'XII'

for i in roman_num:
    res = 0
    if i * 4 in roman_num:
        print('Incorrect number')
        break
    for j in range(len(roman_num)):
        res += rom_dict[roman_num[j]]
        try:
            if rom_dict[roman_num[j]] < rom_dict[roman_num[j + 1]]:
                deduction = rom_dict[roman_num[j]] * 2
                res -= deduction
        except IndexError:
            pass

print(res)


# def rom_num_convert(number):
#     result = 0
#     for i in number:
#         if i * 4 in number:
#             return 'Incorrect number'
#     else:
#         for j in range(len(number)):
#             result += rom_dict[number[j]]
#             try:
#                 if rom_dict[number[j]] < rom_dict[number[j + 1]]:
#                     deduction = rom_dict[number[j]] * 2
#                     result -= deduction
#             except IndexError:
#                 pass
#             return result
#
# #
# if __name__ == '__main__':
#     test_num = 'XXXVIII, XXXVIIII, IIV, XXII, XXIX, XXIIII'
#     for n in test_num.split(', '):
#
#         print(f'{n} >>> {rom_num_convert(n)}')
