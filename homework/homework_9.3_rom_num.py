"""
Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
Наприклад: XXII -> 22
"""
def mapping(element):
    if element == 'I':
        return 1
    if element == 'V':
        return 5
    if element == 'X':
        return 10
    if element == 'L':
        return 50
    if element == 'C':
        return 100
    if element == 'D':
        return 500
    if element == 'M':
        return 1000
    return -1


def roman_converter(rom_input):
    for i in [item for item in set(rom_input)]:
        if i * 4 in rom_input:
            return False
        break

    res = 0
    i = 0
    while i < len(rom_input):
        s1 = mapping(rom_input[i])  # get value of symbol s[index]

        if i + 1 < len(rom_input):
            s2 = mapping(rom_input[i + 1])  # get value of the next symbols s[index]
            if s1 >= s2:  # if the next symbol is lower compared to the previous >> add and get next symbol for analysis
                res = res + s1
                i = i + 1
            else:  # if the next symbol os lower >> deduct and get next symbol for analysis, omitting that symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res


if __name__ == '__main__':

    test_num = 'XXVIIII, III, XXXXV, MCMIV, IV, XXII, XXIX, VII'
    for n in test_num.split(', '):
        result = roman_converter(n)
        if result:
            print(f'{n} >>> {roman_converter(n)}')
        else:
            print(f'{n} >>> Incorrect number')