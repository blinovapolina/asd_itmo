from asd_itmo.lab1.task_2.src.lab1_2 import insertion_sort
from asd_itmo.lab1.utils import test


example_arr = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]

print(f'Пример: {test(insertion_sort, example_arr)}\n')
print(f'Минимум: {test(insertion_sort, min_arr = True)}\n')
print(f'Максимум: {test(insertion_sort, max_arr = True, random_in=(-10 ** 9, 10 ** 9 + 1), range_input = 10 ** 3)}\n')




