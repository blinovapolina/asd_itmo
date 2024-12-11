from lab5.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def move_down(i, n, data, swaps):
    min_index = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] < data[min_index]:
        min_index = left

    if right < n and data[right] < data[min_index]:
        min_index = right

    if i != min_index:
        swaps.append((i, min_index))  # Сохраняем пару обменов
        data[i], data[min_index] = data[min_index], data[i]  # Перестановка
        move_down(min_index, n, data, swaps)  # Рекурсивный вызов


def build_heap(n, nums):
    swaps = []

    for i in range(n // 2 - 1, -1, -1):
        move_down(i, n, nums, swaps)

    return swaps


def result_f(n, nums):
    result = ''
    swaps = build_heap(n, nums)
    print(swaps)
    result += str(len(swaps))
    if swaps:
        for i, j in swaps:
            result += f'\n{i} {j}'
    return result


def task_4(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = (str(n) + "\n" + " ".join(map(str, nums)))
    result = result_f(n, nums)
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(build_heap, n, nums)


if __name__ == '__main__':
    task_4(PATH_INPUT, PATH_OUTPUT)
