import string
# s = 'Olha    Telizhuk  Kyiv      Ukraine          python' # delete whitespace if there are more than 1 whitespace
#
# while '  ' in s:
#     s = s.replace('  ', ' ')
# print(s)


# s = input('text = ')
#
# for i in string.punctuation + ' ': # delete whitespace and clear up punctuation
#     while i + i in s:
#         s = s.replace(i * 2,i)
# print(s)

text ='Olha,Yuliia.Ivan;Inna      Mary,Yehor'
for item in string.punctuation:
    text = text.replace(item, ' ')
    res = text.split()
    clear_text = ', '.join(res)
print(f'Users: {clear_text}')
print(f'Number of active users: {len(res)}')
