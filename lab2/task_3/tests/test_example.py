import time
import tracemalloc
from asd_itmo.lab2.task_3.src.lab2_3 import merge_sort_count


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]

result = merge_sort_count(input_arr, [0] * len(input_arr), 0, len(input_arr) - 1)
print('Время работы: ' + str((time.perf_counter() - start_time) * 1000))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()
