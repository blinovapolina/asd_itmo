from lab1.utils import open_file, write_file, print_input_output, measuring


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def insertion_sort(n, list_arr):
    for i in range(1, n):
        key = list_arr[i]
        j = i - 1
        while j >= 0 and key > list_arr[j]:
            list_arr[j + 1] = list_arr[j]
            j -= 1
        list_arr[j + 1] = key
    return list_arr


def task_3(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = (str(n) + "\n" + " ".join(map(str, nums)))
    result = ' '.join(map(str, insertion_sort(n, nums)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(insertion_sort, n, nums)


if __name__ == '__main__':
    task_3(PATH_INPUT, PATH_OUTPUT)
