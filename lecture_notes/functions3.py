def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


print(fact(6))


# recursion
def factor(n):
    if n == 0:
        return 1
    return n * factor(n - 1)


print(factor(6))


def my_print(n):
    if n == 0:
        return
    print(n)
    my_print(n - 1)


print(my_print(20))


def your_print(n):
    if n == 0:
        return
    your_print(n - 1)
    print(n)


print(your_print(20))
