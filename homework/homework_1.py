"""
1. Write a Python-script that displays the message “Hello world”
"""

print('Hello wold!')

'''
2. Rewrite the first script to display three any messages
'''

print("Hello world!", "My name is Olha", "Let's learn Python", sep='\n')


'''
3. Write a Python-script to reads values for the length and width of a rectangle and returns the area of the rectangle.
'''

length = input('Enter length of rectangle in cm: ')
width = input('Enter width of rectangle in cm: ')
sq = int(length) * int(width)
print(f'The area of the rectangle is {sq} cm2')


'''
4. Write a program that requests the user to enter two numbers and prints the sum, product, difference and quotient of the two numbers.
'''

a = int(input('a= '))
b = int(input('b= '))

print(f'a + b = {a+b}',
      f'a - b = {a-b}',
      f'a * b = {a*b}',
      f'a / b = {a/b}', sep="\n")

'''
5. Write a program that reads in the radius of a circle and prints the circle’s diameter,
circumference and area. Use the constant value 3.14159 for π.
Do these calculations in output statements.
'''

from math import pi

radius = int(input('Enter the radius of a circle: '))

diameter = radius * 2
circumference = round(diameter * pi, 3)
area = round(radius ** radius * pi, 3)

print("The circle diameter is:", diameter)
print("The circle circumference is:", circumference)
print("The circle area is:", area)