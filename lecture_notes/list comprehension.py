import random

for index, item in enumerate(range(100, 111)):
    print(index, item)

z = []
for i in range(10):
    z.append(random.randint(1, 100))
print(z)

# list comprehension
y = [random.randint(1, 100) for i in range(10)]
print(y)

w = [i ** 2 for i in range(10) if not i % 2]
print(w)

