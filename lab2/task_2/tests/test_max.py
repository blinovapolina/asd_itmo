import time
import tracemalloc
import random
from asd_itmo.lab2.task_2.src.lab2_2 import merge_sort_output


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [random.randint(-10 ** 9, 10 ** 9 + 1) for _ in range(10 ** 5)]

result = merge_sort_output(input_arr, [0] * len(input_arr), 0, len(input_arr) - 1, list())
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()