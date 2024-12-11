from lab5.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def heapify(lst, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[left] < lst[smallest]:
        smallest = left

    if right < n and lst[right] < lst[smallest]:
        smallest = right

    if smallest != i:
        lst[i], lst[smallest] = lst[smallest], lst[i]
        heapify(lst, n, smallest)


def heap_sort(n, lst):
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

    return lst


def task_7(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = (str(n) + "\n" + " ".join(map(str, nums)))
    result = " ".join(map(str, heap_sort(n, nums)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(heap_sort, n, nums)


if __name__ == '__main__':
    task_7(PATH_INPUT, PATH_OUTPUT)
