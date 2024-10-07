import time
import tracemalloc
from asd_itmo.lab1.task_5.src.lab1_5 import selection_sort


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [31, 41, 59, 26, 41, 58]

result = selection_sort(len(input_arr), input_arr)
print('Время работы: ' + str((time.perf_counter() - start_time) * 1000))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()