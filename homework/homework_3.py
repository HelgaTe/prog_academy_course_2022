'''
1. Write a Python program to print the number entered by user only if the
number entered is negative.
'''

num = int(input('Enter the number: '))
num < 0 and print(num)

'''
2. Write a Python program to check if the value a is less than 20 or not.
'''

num = int(input('Enter the number: '))

res = num < -20 and 'Yes' or 'No'
print(res)

'''
3: Write a Python program to check if a given number is Zero or Not.
'''

num = int(input('Enter the number: '))

print(num or 'is Zero')
print(not num or 'not Zero')

'''
4. Write a Python program to check if a given number is Even or Odd.
'''

num = int(input('Enter the number: '))

res = not num % 2 and "Even" or "Odd"
print(res)

'''
5. Write a Python program to find largest number among three numbers
entered by user.
'''

a, b, c = int(input('a = ')), int(input('b = ')), int(input('c = '))
print(f'The largest number is: {max(a, b, c)}')


