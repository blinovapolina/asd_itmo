from asd_itmo.lab1.task_6.src.lab1_6 import bubble_sort
from asd_itmo.utils import test


example_arr = [5, 6, 9, 0, 4, 6, 5, 1]

print(f'Пример: {test(bubble_sort, example_arr)}\n')
print(f'Минимум: {test(bubble_sort, min_arr = True)}\n')
print(f'Максимум: {test(bubble_sort, max_arr = True, random_in=(-10 ** 9, 10 ** 9 + 1), range_input = 10 ** 3)}\n')
