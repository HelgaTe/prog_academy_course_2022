"""
Task4:
Создайте декоратор с параметрами для проведения хронометража работы той или иной функции.
Параметрами должны выступать то, сколько раз нужно запустить декорируемую функцию и
в какой файл сохранить результаты хронометража. Цель - провести хронометраж декорируемой функции.
"""

import datetime
from typing import Callable

def time_decorator(func: Callable):
    """
    Calculate run time of the function in a certain range of cycles, save results to
    'run_time_result.txt'.
    Parameters 'cycles' and 'folder' sets inside the function.
    :param func: Function.
    :return: None
    """

    num_of_cycles = 100
    save_to = 'run_time_result.txt'

    def inner(*args, **kwargs):

        date_start = datetime.datetime.now()
        for _ in range(num_of_cycles):
            func(*args, **kwargs)
        date_finish = datetime.datetime.now()

        run_time = date_finish - date_start

        with open(save_to, 'a') as file:
                file.write(f'{func.__name__} '
                           f'Run time: {run_time.seconds}.{run_time.microseconds} sec, '
                           f'Executed: {datetime.datetime.now()}\n')

    return inner


@time_decorator
def expon(a, b):
   return a**b


print(expon(200, 3))
