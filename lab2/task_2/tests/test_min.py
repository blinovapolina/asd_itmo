import time
import tracemalloc
from asd_itmo.lab2.task_2.src.lab2_2 import merge_sort_output


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [0]

result = merge_sort_output(input_arr, [0] * len(input_arr), 0, len(input_arr) - 1, list())
print('Время работы: ' + str((time.perf_counter() - start_time) * 1000))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()
