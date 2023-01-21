"""
Task 2: Використовуючи замикання, реалізуйте <Мемоізація>. Використовуйте отриманий механізм для 
прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.
"""
import timeit

stmt1= """
def recur_fibonacci(n): # recursion approach
    if n <=1:
        return 1
    else:
        return recur_fibonacci((n - 1)) + recur_fibonacci(n - 2)
recur_fibonacci(30)
"""
stmt2 = """
def fibonacci(): # closure approach
    buffer = [1, 1]
    def get_nxt(n):
        if n < len(buffer):
            return buffer[n - 1]

        current, nxt = buffer[-2], buffer[-1]
        index = len(buffer)
        while index <= n:
            current, nxt = nxt, current + nxt
            buffer.append(nxt)
            index += 1
        return nxt

    return get_nxt

f = fibonacci()
f(30)
"""

print(f'Recursion time: {timeit.timeit(stmt1, number=10)}')
print(f'Closure time {timeit.timeit(stmt2, number=10)}')

