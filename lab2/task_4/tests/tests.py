from asd_itmo.lab2.task_4.src.lab2_4 import binary_search
from asd_itmo.lab2.utils import test


example_arr = [1, 5, 8, 12, 13]
search_arr = [8, 1, 23, 1, 11]

print(f'Пример: {test(binary_search, example_arr, search_arr=search_arr)}\n')
print(f'Минимум: {test(binary_search, min_arr = True, search_arr=[0])}\n')
print(f'Максимум: {test(binary_search, max_arr = True, random_in=(-10 ** 9, 10 ** 9 + 1), range_input = 2 * (10 ** 4), search_arr = [i for i in range(10 ** 5, 0, -1)])}\n')
