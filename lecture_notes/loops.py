i = 0
while i < 10:
    print(i + 1, 'Hello')
    i += 1


text = input('Text = ')
while not (text.lower() == 'yes' or text.lower() == 'no'):
    print(text.upper())
    text = input('Text = ')


while True:
    text = input('Tex = ')
    if text.lower() == 'yes' or text.lower() == 'no':
        break
    print(text.upper())


# Перевірити що число просте (це число яке ділиться лише на 1 та на саме число)
n = int(input('n='))

for i in range(2, n):
    if not n % i:
        print('Not prime number')
        break
    else:
        print('Prime number')


