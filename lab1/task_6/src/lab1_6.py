from lab1.utils import open_file, write_file, print_input_output, measuring



PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def bubble_sort(n, A):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


def task_6(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = (str(n) + "\n" + " ".join(map(str, nums)))
    result = ' '.join(map(str, bubble_sort(n, nums)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(bubble_sort, n, nums)


if __name__ == '__main__':
    task_6(PATH_INPUT, PATH_OUTPUT)
