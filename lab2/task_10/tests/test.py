import time
import random
from asd_itmo.lab2.task_10.src.lab2_10 import merge_sort


def insertion_sort(list_arr):
    for i in range(1, len(list_arr)):
        key = list_arr[i]
        j = i - 1
        while j >= 0 and key < list_arr[j]:
            list_arr[j + 1] = list_arr[j]
            j -= 1
        list_arr[j + 1] = key
    return list_arr


def selection_sort(A):
    for i in range(len(A) - 1):
        min_local = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_local]:
                min_local = j
        A[i], A[min_local] = A[min_local], A[i]
    return A


def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time


def find_threshold(max_size):
    for size in range(1, max_size + 1):
        arr = [random.randint(-10 ** 9, 10 ** 9) for _ in range(size)]

        insertion_time = measure_time(insertion_sort, arr.copy())
        selection_time = measure_time(selection_sort, arr.copy())
        merge_time = measure_time(merge_sort, arr.copy())

        print(
            f"Размер: {size} | Merge: {merge_time:.8f}s | Insertion: {insertion_time:.8f}s | Selection: "
            f"{selection_time:.8f}s")

        if merge_time < insertion_time and merge_time < selection_time:
            print(f"Merge sort быстрее, чем insertion sort и selection sort на массиве размером: {size}")
            break


find_threshold(1000)
