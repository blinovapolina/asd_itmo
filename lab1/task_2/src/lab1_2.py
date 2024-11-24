from asd_itmo.lab1.utils import open_file, write_file


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def insertion_sort(n, list_arr):
    index_result = [1]
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if list_arr[i] < list_arr[j]:
                list_arr[i], list_arr[j] = list_arr[j], list_arr[i]
                i, j = j, i
        index_result.append(i + 1)
    return index_result, list_arr


def task_2():
    n, nums = open_file(PATH_INPUT)
    if 1 <= n <= 10 ** 3 and all([abs(n) <= 10 ** 9 for x in nums]):
        write_file(insertion_sort(n, nums), PATH_OUTPUT)
    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_2()
