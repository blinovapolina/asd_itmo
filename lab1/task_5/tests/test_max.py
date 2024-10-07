import time
import tracemalloc
import random
from asd_itmo.lab1.task_5.src.lab1_5 import selection_sort


start_time = time.perf_counter()
tracemalloc.start()
input_arr = [random.randint(-10 ** 9, 10 ** 9 + 1) for _ in range(10 ** 3)]

result = selection_sort(len(input_arr), input_arr)
print('Время работы: ' + str((time.perf_counter() - start_time)))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()