import random
from asd_itmo.lab2.task_3.src.lab2_3 import merge_sort_count
from asd_itmo.lab2.utils import test


example_arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]

print(f'Пример: {test(merge_sort_count, example_arr, temp = [0] * len(example_arr), left_i = 0, right_i = len(example_arr) - 1)}\n')
print(f'Минимум: {test(merge_sort_count, min_arr = True, temp = [0], left_i = 0, right_i = 0)}\n')
print(f'Максимум: {test(merge_sort_count, [random.randint(-10 ** 9, 10 ** 9 + 1) for _ in range(10 ** 5)], temp = [0] * 20000, left_i = 0, right_i = 20000 - 1)}\n')
