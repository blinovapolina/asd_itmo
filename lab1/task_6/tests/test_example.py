import time
import tracemalloc
from asd_itmo.lab1.task_6.src.lab1_6 import bubble_sort


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [5, 6, 9, 0, 4, 6, 5, 1]

result = bubble_sort(len(input_arr), input_arr)
print('Время работы: ' + str((time.perf_counter() - start_time) * 1000))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()