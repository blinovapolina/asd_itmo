import random
from lab3.utils import open_file, write_file, measuring, print_input_output


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def partition(arr, left_index, right_index):
    pivot = arr[left_index]
    j = left_index
    for i in range(left_index + 1, right_index + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[left_index], arr[j] = arr[j], arr[left_index]
    return j


def randomized_quicksort(arr, left_index, right_index):
    if left_index < right_index:
        random_num = random.randint(left_index, right_index)
        arr[left_index], arr[random_num] = arr[random_num], arr[left_index]
        m = partition(arr, left_index, right_index)
        randomized_quicksort(arr, left_index, m - 1)
        randomized_quicksort(arr, m + 1, right_index)
    return arr


def task_1_1(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = str(n) + '\n' + ' '.join(map(str, nums))
    result = ' '.join(map(str, randomized_quicksort(nums, 0, n - 1)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(randomized_quicksort, nums, 0, n - 1)


if __name__ == '__main__':
    task_1_1(PATH_INPUT, PATH_OUTPUT)
