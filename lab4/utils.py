import time
import tracemalloc


def open_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        if len(data) == 1:
            return data[0]
        # elif len(data) == 2:
        #     if ord(data[1][0]) in range(65, 91):
        #         arr = [i for i in data[1]]
        #     else:
        #         arr = list(map(int, data[1].split()))
        #
        #     n = data[0]
        #     if len(n.split()) == 1:
        #         n = int(n)
        #         return n, arr
        #     else:
        #         n, k =map(int, n.split())
        #         return n, k, arr
        # elif len(data) == 3:
        #     n, m = map(int, data[0].split())
        #     a = list(map(int, data[1].split()))
        #     b = list(map(int, data[2].split()))
        #     return n, m, a, b
        elif len(data[1:]) == int(data[0]):
            n = int(data[0].rstrip())
            list_input = list(data[i].rstrip() for i in range(1, n + 1))
            return n, list_input
        # else:
        #     n, k = map(int, data[0].split())
        #     intervals = [list(map(int, i.split())) for i in data[1:n + 1]]
        #     dots = list(map(int, data[n + 1].split()))
        #     return n, k, intervals, dots


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


def measuring(task_func, *args):
    start_time = time.perf_counter()
    tracemalloc.start()

    task_func(*args)
    print(f'Время работы: {time.perf_counter() - start_time}\n'
          f'Память: {str(tracemalloc.get_traced_memory()[1] / 1024 ** 2)} Мб')
    tracemalloc.stop()


def print_input_output(inputs=str, result=str):
    print(f'Входные данные: \n{inputs}')
    print(f'Результат: \n{result}')