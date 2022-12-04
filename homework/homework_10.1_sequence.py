"""
Існують такі послідовності чисел:
0,2,4,6,8,10,12
1,4,7,10,13
1,2,4,8,16,32
1,3,9,27
1,4,9,16,25
1,8,27,64,125
Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
Послідовність користувач вводить з клавіатури у вигляді рядка. Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.
"""


def step_2(seq):
    new_seq = [seq[j] + 2 for j in range(len(seq))]
    if seq[1::] == new_seq[:len(new_seq) - 1]:
        return new_seq[-1]


def step_3(seq):
    new_seq = [seq[j] + 3 for j in range(len(seq))]
    if seq[1::] == new_seq[:len(new_seq) - 1]:
        return new_seq[-1]


def multiply_2(seq):
    new_seq = [seq[j] * 2 for j in range(len(seq))]
    if seq[1::] == new_seq[:len(new_seq) - 1]:
        return new_seq[-1]


def multiply_3(seq):
    new_seq = [seq[j] * 3 for j in range(len(seq))]
    if seq[1::] == new_seq[:len(new_seq) - 1]:
        return new_seq[-1]


def exponentiation_2(seq):
    new_seq = [seq[j] ** (1 / 2) for j in range(len(seq))]
    new_seq = [(item + 1) ** 2 for item in new_seq]
    if seq[1::] == new_seq[:len(new_seq) - 1]:
        return new_seq[-1]


def exponentiation_3(seq):
    new_seq = [seq[j] ** (1 / 3) for j in range(len(seq))]
    new_seq = [round((i + 1)) ** 3 for i in new_seq]
    if seq[1::] == new_seq[:len(new_seq) - 1]:
        return new_seq[-1]


if __name__ == '__main__':
    sequence = [
        [0, 2, 4, 6, 8, 10, 12, 14, 16],
        [1, 4, 7, 10, 13, 16, 19],
        [1, 2, 4, 8, 16, 32, 64],
        [1, 3, 9, 27, 81],
        [1, 4, 9, 16, 25, 36, 49],
        [1, 8, 27, 64, 125, 216, 343]
    ]
    seq_analyzer = [
        step_2,
        step_3,
        multiply_2,
        multiply_3,
        exponentiation_2,
        exponentiation_3
    ]

    for item in sequence:
        for func in seq_analyzer:
            if func(item):
                print(f'{item}, next element  << {func(item)} >>')
