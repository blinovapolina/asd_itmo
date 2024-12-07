from lab3.utils import open_file, write_file, measuring, print_input_output
from lab3.task_1.src.lab3_1_1 import randomized_quicksort


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def summa_ten_sort(a, b):
    list_got = [el_a * el_b for el_a in a for el_b in b]
    randomized_quicksort(list_got, 0, len(list_got) - 1)
    summa_ten = sum(list_got[i] for i in range(0, len(list_got), 10))
    return summa_ten


def task_6(input_file, output_file):
    n, m, list_a, list_b = open_file(input_file)
    inputs = (str(n) + ' ' + str(m) + '\n' + " ".join(map(str, list_a)) +
              '\n' + " ".join(map(str, list_b)))
    result = str(summa_ten_sort(list_a, list_b))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(summa_ten_sort, list_a, list_b)


if __name__ == '__main__':
    task_6(PATH_INPUT, PATH_OUTPUT)
