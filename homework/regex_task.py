"""
Task 1: Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R,
за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
"""

import re

text = 'Hello 896 # -  Rbr,  RR rBr rbR. Nice # to dd - rr R meet you - Rbbr rBBr; rbbbR.\nRrbBbr & RbBbr\nRbbbb rbBbr !'

regex = r'[Rr][Bb]{1,}[Rr]'
result = re.findall(regex,text)
print(f'Task 1: {result}')


"""
Task 2: Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
"""
cards = ['9999-9999-9999-9999',
         '1234_1234_1234_1234',
         'aa99-123-1234-1234',
         '9999-f0a9-9999-9999',
         '1234123412341234'
         '123#-1234-1234-1234']

regex_2 = r'(?:\d{4}[_-]?){3}\d{4}'

cards_str = ', '.join(cards)
cards = re.findall(regex_2, cards_str)
print(f'Task 2: {cards}')

"""
Task 3: Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
Вимоги:
** Цифри (0-9).
** лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
** у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
"""

mails = ['olga@gmail.com',
         'olga@global.com',
         '-olha@global.com',
         'olga@telizhuk@gmail.com',
         'ol__ga@gmail.com',
         'olga15..@gmail.com',
         'olga-t@gmail.com',
         'olga--t@gmai.com',
         'olga_15$.@gmail.com']

mail_str = ', '.join(mails)

regex_3 = r'[a-zA-Z09]*[_-]?[a-zA-Z0-9]?@\w+.com'

valid_emails = []
res = re.findall(regex_3, mail_str)
for item in res:
    for n in range(len(mails)):
        if item == mails[n]:
            valid_emails.append(item)

print(f'Task 3: {valid_emails}')


"""
Task 4: Напишіть функцію, яка перевіряє правильність логіну. 
Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.
"""

login1 = 'olga01'
login2 =  'olga_01'
login3 = 'olga1234567'
login4 = 'olga123456'

regex_4 = r'^[a-zA-Z0-9]{2,10}$'
check1 = re.findall(regex_4, login1)
check2 = re.findall(regex_4, login2)
check3 = re.findall(regex_4, login3)
check4 = re.findall(regex_4, login4)

print(f'Task 4: {check1} {check2} {check3} {check4}')




