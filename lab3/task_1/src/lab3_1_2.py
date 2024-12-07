import random
from lab3.utils import open_file, write_file, measuring, print_input_output


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def partition_upd(arr, left_index, right_index):
    x = arr[left_index]
    m_left = left_index
    m_right = right_index
    i = left_index

    while i <= m_right:
        if arr[i] < x:
            arr[m_left], arr[i] = arr[i], arr[m_left]
            m_left += 1
            i += 1
        elif arr[i] > x:
            arr[i], arr[m_right] = arr[m_right], arr[i]
            m_right -= 1
        else:
            i += 1

    return m_left, m_right


def randomized_quicksort(arr, left_index, right_index):
    if left_index < right_index:
        random_num = random.randint(left_index, right_index)
        arr[left_index], arr[random_num] = arr[random_num], arr[left_index]
        m1, m2 = partition_upd(arr, left_index, right_index)
        randomized_quicksort(arr, left_index, m1 - 1)
        randomized_quicksort(arr, m2 + 1, right_index)
    return arr


def task_1_2(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = str(n) + '\n' + ' '.join(map(str, nums))
    result = ' '.join(map(str, randomized_quicksort(nums, 0, n - 1)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(randomized_quicksort, nums, 0, n - 1)


if __name__ == '__main__':
    task_1_2(PATH_INPUT, PATH_OUTPUT)
