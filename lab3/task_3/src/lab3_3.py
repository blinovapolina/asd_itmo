from lab3.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def pugalo_sort(n, k, nums):
    for i in range (0, n - k):
        if nums[i] > nums[i + k]:
            nums[i], nums[i + k] = nums[i + k], nums[i]
    return "ДА" if nums == sorted(nums) else "НЕТ"


def task_3(input_file, output_file):
    n, k, nums = open_file(input_file)
    inputs = str(n) + ' ' + str(k) + '\n' + " ".join(map(str, nums))
    result = pugalo_sort(n, k, nums)
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(pugalo_sort, n, k, nums)


if __name__ == '__main__':
    task_3(PATH_INPUT, PATH_OUTPUT)
