def func(a):
    while a > 0:
        yield a
        a -= 1


x = func(10)
print(x)  # stdout <generator object>
print(next(x))
print(next(x))
print(next(x))
print('=' * 40)

for item in func(3):
    print(item)
print('=' * 40)


def fibonacci(n):  # generator func >> elements are not kept in memory
    prev, curr, = 0, 1
    index = 0
    while index < n:
        yield curr
        prev, curr = curr, prev + curr
        index += 1


for i in fibonacci(10):
    print(i)

x = list(fibonacci(10))  # sequence, elements are not kept in memory
print(x)







