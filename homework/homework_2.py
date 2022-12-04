'''
1. Construct an integer from the string "123"
'''

str1 = '123'
int1 = int(str1)

'''
2. Construct a float from the integer 123
'''

float1 = float(int1)
print(float1)

'''
3. Construct an integer from the float 12.345
'''
float2 = 12.345
int2 = int(float2)

'''
4. Write a Python-script that detects the last 4 digits of a credit card
'''

# ver1
card_num = input("Enter a credit card number: ") # 1234567812345678
last_nums = card_num[-4:]
print(last_nums)

# ver2
card_num2 = int(input('Card number: ')) # 6767_8989_0909_4545
print(card_num2 % 10_000)

'''
5. Write a Python-script that calculates the sum of the digits of a three-digit number
'''

num = int(input('Enter three-digit number: '))

num1 = num//100 # divide nums and round the result down to the nearest whole number >>> the 1st digit num
num3 = num % 10 # gives the remainder when the first number is divided from the second number >>> the 3rd digit num
num2 = num //10 % 10
num_sum = num1 + num2 + num3

print(num1, num2, num3, sep='\n')
print(f'The sum of the digits : {num_sum}')
'''
6. Write a program that calculates and displays the area of a triangle if its sides are known
'''

# triangle sides are known:
a, b, c = 3, 6, 7

p = (a+b+c)/2  # perimeter of the triangle
area = (p*(p-a)*(p-b)*(p-c))**0.5 # the area of the triangle
area = round(area, 3) # simplify the number, but keep it close to initial result

print(f'The area of a triangle is: {area}')

'''
7. Write a Python-script that calculates the sum of the digits of a number
'''

num = input("Input number: ")

digits = list(num)
total = 0
for d in digits:
    d = int(d)
    total += d

print(f'The sum of the digits: {total}')

'''
8. Determine the number of digits in a number
'''

num = input("Input number: ")

num_length = len(num)
print(f'The number of digits in a number: {num_length}')


'''
9. Print the digits in reverse order
'''

num = input("Input number: ")

rev_order = ''
for digit in num:
    rev_order = digit + rev_order
print(f'The original number is: {num}')
print(f'The reverse order of number is: {rev_order}')

