from lab2.utils import open_file, write_file, measuring, print_input_output


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


def task_2(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = str(n) + '\n' + ' '.join(map(str, nums))
    res = list()
    merge_sort_output(nums, [0] * n, 0, n - 1, res)
    result = "\n".join(map(str, res)) + '\n' + " ".join(map(str, nums))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(merge_sort_output, nums, [0] * n, 0, n - 1, res)


if __name__ == "__main__":
    task_2(PATH_INPUT, PATH_OUTPUT)
