import time
import tracemalloc
import random
from asd_itmo.lab2.task_10.src.lab2_10 import merge_sort


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [random.randint(-10 ** 9, 10 ** 9 + 1) for _ in range(2 * (10 ** 4))]

result = merge_sort(input_arr)
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()