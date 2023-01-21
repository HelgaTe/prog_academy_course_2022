"""
Task 3: Напишіть функцію, яка застосує до списку чисел довільну функцію користувача 
і поверне суми елементів отриманого списку.
"""
def func(item):
    return item ** 3

def user_rule(seq, funct):
    result = sum (funct(i) for i in seq)
    return result

x = [1, 2, 3, 4, 5]
res = user_rule(x, func)
print(f'User rule result | defined func: {res}')
res2 = user_rule(x, lambda item: item * 10)
print(f'User rule result | lambda: {res2}')
