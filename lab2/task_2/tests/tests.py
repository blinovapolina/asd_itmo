import random
from asd_itmo.lab2.task_2.src.lab2_2 import merge_sort_output
from asd_itmo.utils import test


example_arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]

print(f'Пример: {test(merge_sort_output, example_arr, temp = [0] * len(example_arr), left_i = 0, right_i = len(example_arr) - 1, res = list())}\n')
print(f'Минимум: {test(merge_sort_output, min_arr = True, temp = [0], left_i = 0, right_i = 0, res = list())}\n')
print(f'Максимум: {test(merge_sort_output, [random.randint(-10 ** 9, 10 ** 9 + 1) for _ in range(10 ** 5)],  temp = [0] * (100000), left_i = 0, right_i = 100000 - 1, res = list())}\n')
