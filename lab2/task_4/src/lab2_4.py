from asd_itmo.lab2.utils import open_file, write_file, measuring


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


def search_elements(array, targets):
    result = []
    for target in targets:
        index = binary_search(array, target)
        result.append(index)
    return result


def task_4():
    n, nums, k, list_search = open_file(PATH_INPUT)
    if 1 <= n <= 10 ** 5 and 1 <= k <= 10 ** 5 and all([abs(n) <= 10 ** 9 for _ in nums]):
        write_file(search_elements(nums, list_search), PATH_OUTPUT)
        measuring(search_elements, nums, list_search)
    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_4()

