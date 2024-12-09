from lab1.utils import open_file, write_file, print_input_output, measuring


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def selection_sort(n, A):
    for i in range(n - 1):
        min_local = i
        for j in range(i + 1, n):
            if A[j] < A[min_local]:
                min_local = j
        A[i], A[min_local] = A[min_local], A[i]
    return A


def task_5(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = (str(n) + "\n" + " ".join(map(str, nums)))
    result = ' '.join(map(str, selection_sort(n, nums)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(selection_sort, n, nums)


if __name__ == '__main__':
    task_5(PATH_INPUT, PATH_OUTPUT)
