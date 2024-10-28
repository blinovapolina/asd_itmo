import random
from asd_itmo.lab2.task_5.src.lab2_5 import majority
from asd_itmo.utils import test


example_arr = [2, 3, 9, 2, 2]

print(f'Пример: {test(majority, example_arr)}\n')
print(f'Минимум: {test(majority, [0])}\n')
print(f'Максимум: {test(majority, [random.randint(-10 ** 9, 10 ** 9 + 1) for _ in range(10 ** 5)])}')
