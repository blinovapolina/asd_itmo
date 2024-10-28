from asd_itmo.lab1.task_1.src.lab1_1 import insertion_sort
from asd_itmo.utils import test


example_arr = [31, 41, 59, 26, 41, 58]

print(f'Пример: {test(insertion_sort, example_arr)}\n')
print(f'Минимум: {test(insertion_sort, min_arr = True)}\n')
print(f'Максимум: {test(insertion_sort, max_arr = True, random_in=(-10 ** 9, 10 ** 9 + 1), range_input = 10 ** 3)}\n')
