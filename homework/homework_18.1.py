"""
Task 1:
Создайте декоратор, который будет подсчитывать, сколько раз была
вызвана декорируемая функция.
"""
def call_counter(f):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count +=1
        print(f'Function {f.__name__} was called {count} time(s)')
        return f(*args, *kwargs)
    return inner
@call_counter
def suma(a, b):
    return a + b

print(suma(10,3))
print(suma(5,17))
print(suma(13,56))
print(suma(78,9))
print(suma(34,27))



