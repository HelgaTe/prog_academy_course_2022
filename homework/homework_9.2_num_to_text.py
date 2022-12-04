"""
Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат.
Наприклад:
> 123,34
> one hundred twenty three dollars thirty four cents
"""
num_in_words = {
    '1': 'one',
    '2': 'two',
    '3': 'thee',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'fourty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety'
}


# 3 digits numbers are accepted only
def price_to_text(price_num):
    dollar, cent = price_num.split('.')
    # dollar part of price
    h = int(dollar) // 100
    o = int(dollar) % 10
    t = int(dollar) % 100 - o

    if len(dollar) == 3:
        hundred = f'{num_in_words[str(h)]} hundred'

    if str(t).startswith('10'):
        num = str(t + o)
        tens = f'{num_in_words[str(num)]}'
    elif not str(t).startswith('1'):
        tens = f'{num_in_words[str(t)]} {num_in_words[str(o)]}'
    else:
        tens = f'{num_in_words[str(t)]}'

    if hundred:
        dollars = f'{hundred} {tens} dollars'
    else:
        dollars = f'{tens} dollars'

    # cent part of price
    oc = int(cent) % 10
    tc = int(cent) - oc

    if str(tc).startswith('10'):
        num = str(tc + oc)
        ten_c = f'{num_in_words[str(num)]}'
    elif not str(tc).startswith('1'):
        ten_c = f'{num_in_words[str(tc)]} {num_in_words[str(oc)]}'
    else:
        ten_c = f'{num_in_words[str(tc)]}'
    cents = f'{ten_c} cents'

    text = f'{dollars} {cents}'
    return text


# price = str(input('price = ').replace(',', '.'))
price2 = '911.17'
print(price_to_text(price2))
