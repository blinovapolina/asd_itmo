from asd_itmo.lab2.utils import open_file, write_file, measuring


PATH_INPUT = '../txtf/input_1.txt'
PATH_OUTPUT = '../txtf/output.txt'


def find_majority(list_arr, left_i, right_i):
    if left_i == right_i:
        return list_arr[left_i]

    middle_arr = (left_i + right_i) // 2

    if left_i == middle_arr:
        left = list_arr[left_i]
    else:
        left = find_majority(list_arr, left_i, middle_arr)

    if middle_arr + 1 == right_i:
        right = list_arr[right_i]
    else:
        right = find_majority(list_arr, middle_arr + 1, right_i)

    counter_left, counter_right = 0, 0
    for i in range(left_i, right_i + 1):
        if list_arr[i] == right:
            counter_right += 1
        elif list_arr[i] == left:
            counter_left += 1
    return left if counter_left > counter_right else right


def majority(n, list_arr):
    result = find_majority(list_arr, 0, len(list_arr) - 1)
    if result:
        if list_arr.count(result) > n / 2:
            return 1
    return 0


def task_5():
    n, nums = open_file(PATH_INPUT)
    if 1 <= n <= 10 ** 5 and all([abs(n) <= 10 ** 9 for _ in nums]):
        write_file(str(majority(n, nums)), PATH_OUTPUT)
        measuring(majority, n, nums)
    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_5()



