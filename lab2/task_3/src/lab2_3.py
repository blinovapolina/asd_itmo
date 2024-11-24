from asd_itmo.lab2.utils import open_file, write_file, measuring


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def merge_count(arr, temp_arr, left, mid, right):
    inversion_counter = 0

    left_i = left
    right_i = mid + 1
    merged_i = left

    while left_i <= mid and right_i <= right:
        if arr[left_i] <= arr[right_i]:
            temp_arr[merged_i] = arr[left_i]
            left_i += 1
        else:
            temp_arr[merged_i] = arr[right_i]
            inversion_counter += (mid - left_i + 1)
            right_i += 1
        merged_i += 1

    while left_i <= mid:
        temp_arr[merged_i] = arr[left_i]
        left_i += 1
        merged_i += 1

    while right_i <= right:
        temp_arr[merged_i] = arr[right_i]
        right_i += 1
        merged_i += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inversion_counter


def merge_sort_count(list_arr, temp, left_i, right_i):
    inversion_counter = 0

    if left_i < right_i:
        middle = (left_i + right_i) // 2

        inversion_counter += merge_sort_count(list_arr, temp, left_i, middle)
        inversion_counter += merge_sort_count(list_arr, temp, middle + 1, right_i)
        inversion_counter += merge_count(list_arr, temp, left_i, middle, right_i)
    return inversion_counter


def task_3():
    n, nums = open_file(PATH_INPUT)
    if 1 <= n <= 2 * (10 ** 4) and all([abs(n) <= 10 ** 9 for _ in nums]):
        write_file(str((merge_sort_count(nums, [0] * n, 0, n - 1))), PATH_OUTPUT)
        measuring(merge_sort_count, nums, [0] * n, 0, n - 1)
    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_3()
