from lab3.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def anti_qsort(n):
    list_ranged = list(range(1, n + 1))
    for i in range(2, n):
        list_ranged[i], list_ranged[i // 2] = list_ranged[i // 2], list_ranged[i]
    return list_ranged


def task_2(input_file, output_file):
    n = open_file(input_file)
    inputs = str(n)
    result = ' '.join(map(str, anti_qsort(n)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(anti_qsort, n)


if __name__ == '__main__':
    task_2(PATH_INPUT, PATH_OUTPUT)
