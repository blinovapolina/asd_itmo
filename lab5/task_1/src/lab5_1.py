from lab5.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def is_heap(n, array):
    for i in range(n):
        if 2 * i + 1 < n and array[i] > array[2 * i + 1]:
            return "NO"
        if 2 * i + 2 < n and array[i] > array[2 * i + 2]:
            return "NO"
    return "YES"



def task_1(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = (str(n) + "\n" + " ".join(map(str, nums)))
    result = is_heap(n, nums)
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(is_heap, n, nums)


if __name__ == '__main__':
    task_1(PATH_INPUT, PATH_OUTPUT)
