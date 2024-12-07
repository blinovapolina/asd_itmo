from lab2.utils import open_file, write_file, measuring, print_input_output


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def binary_search(list_arr, number):
    left, right = 0, len(list_arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_arr[middle] == number:
            return middle
        elif list_arr[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def search_elements(array, targets):
    result = []
    for target in targets:
        index = binary_search(array, target)
        result.append(index)
    return result


def task_4(input_file, output_file):
    n, nums, k, list_search = open_file(input_file)
    inputs = str(n) + '\n' + ' '.join(map(str, nums)) +'\n' + str(k) + ' '.join(map(str, list_search))
    result = ' '.join(map(str, search_elements(nums, list_search)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(search_elements, nums, list_search)


if __name__ == "__main__":
    task_4(PATH_INPUT, PATH_OUTPUT)
