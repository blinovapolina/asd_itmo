from lab2.utils import open_file, write_file, measuring, print_input_output


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def merge(left, right):
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


def merge_sort(n, list_arr):
    if len(list_arr) <= 1:
        return list_arr

    middle = len(list_arr) // 2
    left_list = merge_sort(len(list_arr[:middle]), list_arr[:middle])
    right_list = merge_sort(len(list_arr[middle:]), (list_arr[middle:]))
    return merge(left_list, right_list)


def task_1(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = str(n) + '\n' + ' '.join(map(str, nums))
    result = ' '.join(map(str, merge_sort(n, nums)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(merge_sort, n, nums)


if __name__ == "__main__":
    task_1(PATH_INPUT, PATH_OUTPUT)
