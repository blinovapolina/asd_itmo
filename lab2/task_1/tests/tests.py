from asd_itmo.lab2.task_1.src.lab2_1 import merge_sort
from asd_itmo.utils import test


example_arr = [12, 52, 0, 7, 9, 1]

print(f'Пример: {test(merge_sort, example_arr)}\n')
print(f'Минимум: {test(merge_sort, min_arr = True)}\n')
print(f'Максимум: {test(merge_sort, max_arr = True, random_in=(-10 ** 9, 10 ** 9 + 1), range_input = 2 * (10 ** 4))}\n')
