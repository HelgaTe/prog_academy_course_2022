import random
import timeit

x = (i ** 2 for i in range(10))  # (<generator object>) sequence, elements are not kept in memory
print(x)
print(sum(x))
x = (i ** 2 for i in range(10))
for item in x:
    print(item)

y = [i ** 2 for i in range(10)]  # list, sequence, elements are kept in memory
print(y)


f = open('text.txt', 'w')  # upload file content into memory
for _ in range(1_000_000):
    f.write(f'{random.randint(1, 100)}\n')
f.flush()
f.close()

stmt_1 = """
with open('text.txt') as f:  # line by line file content reading - work as with sequence
    data = f.readlines()
    s = 0
    for item in data:
        if item.strip().isdigit():
            s += int(item.strip())
"""

stmt_2 = """
with open('text.txt') as f:  # work as with generator object
    s = 0
    for item in f:
        if item.strip().isdigit():
            s += int(item.strip())
"""

stmt_3 = """
with open('text.txt') as f:
    s = sum(int(item.strip()) for item in f if item.strip().isdigit())
"""

print(timeit.timeit(stmt_1, number=20))
print(timeit.timeit(stmt_2, number=20))
print(timeit.timeit(stmt_3, number=20))
