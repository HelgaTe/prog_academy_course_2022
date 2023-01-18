def func(x: int):
    pass

print(func.__annotations__)

def calculate_pow(b):
    def calcul(a):
        return a ** b
    return calcul

result = calculate_pow(5)
for i in range(2, 6):
    print(result(i))

print('='*40)
def fibonacci():
    a, b = 0, 1
    def next_elem():
        nonlocal a, b
        a, b = b, a + b
        return a
    return next_elem

result = fibonacci()
for _ in range(10):
    print(result())

print('='*40)



