# перевірити чи введене число - просте число
# (просте число має тільки два дільника без остачі - 1 і саме число)

num = int(input('n = '))

for i in range(2,num):
    if not num % i:
        print('Not prime')
        break
else:
    print('Prime')


x = ['a', 'b', 'c', 'd']

for index, item in enumerate(x):
    x[index] = f'{item}*'
    # del x[index]
print(x)

x=[(3,4), (5,6), (7,8), (2,3), (6,5)]

for a,b in x:
    print(f'x={a}; y={b}')

x = [(3, 4, 0, 1, 2, 3), (5, 6, 4, 6, 7, 9), (7, 8, 0, 8, 8), (2, 3, 4, 4, 2), (6, 5, 5, 3, 2, 4)]

for a, b, *z in x:  # <*z> ignore unused items
    print(f'x={a}; y={b}')
    # print(z)

product = [1, 2, 3, 4, 5]
price = [10, 20, 30, 40, 50]
total = 0

for item, quantity in enumerate(product):
    total += quantity * price[item]
# for quantity, price in zip(product,price):
#     total += quantity * price

print(total)


x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]]

for row in x:
    print(sum(row))
