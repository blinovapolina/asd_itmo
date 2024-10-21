import time
import tracemalloc
from asd_itmo.lab2.task_10.src.lab2_10 import merge_sort


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [12, 52, 0, 7, 9, 1]

result = merge_sort(input_arr)
print('Время работы: ' + str((time.perf_counter() - start_time) * 1000))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()
