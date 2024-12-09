from lab1.utils import open_file, write_file, print_input_output, measuring


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def insertion_sort(n, list_arr):
    index_result = [1]
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if list_arr[i] < list_arr[j]:
                list_arr[i], list_arr[j] = list_arr[j], list_arr[i]
                i, j = j, i
        index_result.append(i + 1)
    return index_result, list_arr


def task_2(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = (str(n) + "\n" + " ".join(map(str, nums)))
    result = '\n'.join(map(str, insertion_sort(n, nums)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(insertion_sort, n, nums)


if __name__ == '__main__':
    task_2(PATH_INPUT, PATH_OUTPUT)