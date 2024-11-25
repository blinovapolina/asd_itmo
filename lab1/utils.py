import time
import tracemalloc
import random


def open_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        if len(data) == 2:
            n = int(data[0])
            if ord(data[1][0]) in range(65, 91):
                arr = [i for i in data[1]]
            else:
                arr = list(map(int, data[1].split()))
            return n, arr
        if len(data) == 4:
            n1 = int(data[0])
            n2 = int(data[2])
            arr1 = list(map(int, data[1].split()))
            arr2 = list(map(int, data[3].split()))
            return n1, arr1, n2, arr2
        else:
            n = int(data[0].strip())
            arr1 = list()
            for i in range(1, n + 1):
                row = list(map(int, data[i].strip().split()))
                arr1.append(row)
            arr2 = list()
            for i in range(n + 1, 2 * n + 1):
                row = list(map(int, data[i].strip().split()))
                arr2.append(row)
        return arr1, arr2


def write_file(arr, file_name):
    with open(file_name, 'w') as file:
        if arr == str(arr):
            file.write(arr)
        else:
            if isinstance(arr, list):
                if isinstance(arr[0], list):
                    for r in arr:
                        file.write(' '.join(map(str, r)) + '\n')
                else:
                    file.write(' '.join(map(str, arr)))
            elif isinstance(arr, tuple):
                file.write(f"{' '.join(map(str, arr[0]))}\n")
                file.write(' '.join(map(str, arr[1])))
            else:
                file.write(arr)


def test(function, arr=[], min_input=False, max_input=False, **kwargs):
    if min_input:
        arr = [0]
    elif max_input:
        arr = list(random.randint(kwargs['random_in']) for _ in range(kwargs['range_input']))

    start_time = time.perf_counter()
    tracemalloc.start()

    if 'temp' in kwargs.keys() and 'left_i' in kwargs.keys() and 'right_i' in kwargs.keys() and 'res' in kwargs.keys():
        function(arr, kwargs['temp'], kwargs['left_i'], kwargs['right_i'], kwargs['res'])
    elif 'temp' in kwargs.keys() and 'left_i' in kwargs.keys() and 'right_i' in kwargs.keys():
        function(arr, kwargs['temp'], kwargs['left_i'], kwargs['right_i'])
    elif 'search_arr' in kwargs.keys():
        for number in kwargs['search_arr']:
            function(arr, number)
    else:
        function(len(arr), arr)

    return_text = f'Время работы: {time.perf_counter() - start_time}\n ' \
                  f'Память: {str(tracemalloc.get_traced_memory()[1] / 1024)} Кб'
    tracemalloc.stop()
    return return_text
