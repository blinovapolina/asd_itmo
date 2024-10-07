import time
import tracemalloc
from asd_itmo.lab1.task_2.src.lab1_2 import insertion_sort


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [0]

result = insertion_sort(len(input_arr), input_arr)
print('Время работы: ' + str((time.perf_counter() - start_time) * 1000))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()