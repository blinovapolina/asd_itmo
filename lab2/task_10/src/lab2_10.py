from asd_itmo.lab2.utils import open_file, write_file, measuring


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def merge(left, right):
    if left[-1] <= right[0]:
        return left + right

    list_merged = list()
    left_i = right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                list_merged.append(left[left_i])
                left_i += 1
            else:
                list_merged.append(right[right_i])
                right_i += 1

    while left_i < len(left):
        list_merged.append(left[left_i])
        left_i += 1

    while right_i < len(right):
        list_merged.append(right[right_i])
        right_i += 1

    return list_merged


def merge_sort(list_arr):
    if len(list_arr) <= 1:
        return list_arr

    middle = len(list_arr) // 2
    left_list = merge_sort(list_arr[:middle])
    right_list = merge_sort(list_arr[middle:])
    return merge(left_list, right_list)


def task_10():
    n, nums = open_file(PATH_INPUT)
    if 1 <= n <= 10 ** 5 and all([abs(n) <= 10 ** 9 for _ in nums]):
        write_file(merge_sort(nums), PATH_OUTPUT)
        measuring(merge_sort, nums)
    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_10()





