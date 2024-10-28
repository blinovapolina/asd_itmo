from asd_itmo.utils import open_file, write_file


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def binary_search(list_arr, number):
    left, right = 0, len(list_arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_arr[middle] == number:
            return middle
        elif list_arr[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def task_4():
    n, nums, k, list_search = open_file(PATH_INPUT)
    if 1 <= n <= 10 ** 5 and 1 <= k <= 10 ** 5 and all([abs(n) <= 10 ** 9 for _ in nums]):
        write_file([binary_search(nums, number) for number in list_search], PATH_OUTPUT)
    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_4()

