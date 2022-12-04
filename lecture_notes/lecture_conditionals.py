money = int(input('money='))

apple = 20
orange = 30

if money >= apple + orange:
    print('You can buy apples and oranges')
elif money >= 30:
    print('Apples or oranges')
elif money >= 20:
    print('Only apples')
else:
    print('Have a nice day!')


n = int(input('n = '))
if n < 0:
    n=0
    print(n)
    print('Negative turned to zero')
elif not n:
    print('Zero')
else:
    print('No')