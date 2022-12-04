"""
Реалізуйте функцію, параметрами якої є два числа та рядок.
Повертає вона конкатенацію рядка із сумою чисел
"""


def concatenation(a, b, seq):
    if isinstance(a, int) and isinstance(b, int):
        suma = a + b
        res = str(suma) + seq
    return res


print(concatenation(10, 20, 'olga'))

"""
Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*». 
Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.
"""


def draw(h, w):
    result = f"{'*' * w}\n" + \
             f"*{' ' * (w - 2)}*\n" * (h - 2) + \
             '*' * w
    return result


print(draw(10, 6))

"""
Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел 
Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1»
"""


def search(seq, x):
    for item, index in enumerate(seq):
        if item == x:
            return index
    return -1


x = [100, 122, 53, 4, 75, 96, 37, 48, 95, 80]
res = search(x, 4)

"""
Напишіть функцію, яка поверне кількість слів у текстовому рядку
"""
import string


def num_words(text):
    for i in string.punctuation:
        text = text.replace(i, ' ')
        res = len(text.split())
    return res


print(num_words('Olha, Telizhuk; python. course for beginners'))

"""
Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. 
Наприклад:
> 123,34
> one hundred twenty three dollars thirty four cents
"""
# pip install num2word # install module to convert numbers into words
import num2word


def num_in_words(price_num):
    dollar, cent = price_num.split('.')
    result = f'{num2word.word(dollar).lower()} dollars ' \
             f'{num2word.word(cent).lower()} cents'
    return result


price = str(input('price = ').replace(',', '.'))

print(num_in_words(price))


