import time
import tracemalloc
from asd_itmo.lab2.task_5.src.lab2_5 import majority


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [2, 3, 9, 2, 2]

result = majority(input_arr)
print('Время работы: ' + str((time.perf_counter() - start_time) * 1000))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()
