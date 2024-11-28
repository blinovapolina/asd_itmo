from lab2.utils import open_file, write_file, measuring


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def merge_output(arr, temp_arr, left, mid, right, res):
    left_i = left
    right_i = mid + 1
    merged_i = left

    while left_i <= mid and right_i <= right:
        if arr[left_i] <= arr[right_i]:
            temp_arr[merged_i] = arr[left_i]
            left_i += 1
        else:
            temp_arr[merged_i] = arr[right_i]
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

    if (right - left + 1) > 1:
        res.append(f"{left + 1} {right + 1} {arr[left]} {arr[right]}")


def merge_sort_output(list_arr, temp, left_i, right_i, res):
    if left_i < right_i:
        middle = (left_i + right_i) // 2

        merge_sort_output(list_arr, temp, left_i, middle, res)
        merge_sort_output(list_arr, temp, middle + 1, right_i, res)
        merge_output(list_arr, temp, left_i, middle, right_i, res)


def task_2():
    n, nums = open_file(PATH_INPUT)
    if 1 <= n <= 2 * (10 ** 4) and all([abs(n) <= 10 ** 9 for _ in nums]):
        print(f'Входные данные: \n{n}\n{" ".join(map(str, nums))}')
        res = list()
        merge_sort_output(nums, [0] * n, 0, n - 1, res)
        for num_line in res:
            write_file(num_line + "\n", PATH_OUTPUT)
        write_file(" ".join(map(str, nums)), PATH_OUTPUT)
        print('Результат:\n' + "\n".join(map(str, res)) + '\n' + " ".join(map(str, nums)))
        measuring(merge_sort_output, nums, [0] * n, 0, n - 1, res)

    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_2()





