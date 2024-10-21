import time
import tracemalloc
from asd_itmo.lab2.task_4.src.lab2_4 import binary_search


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [0]
search_arr = [0]

result = [binary_search(input_arr, number) for number in search_arr]
print('Время работы: ' + str((time.perf_counter() - start_time) * 1000))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()
