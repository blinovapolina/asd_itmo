import math
from lab6.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def is_fibonacci_number(number):
    x = int(number)
    f1 = 5 * x ** 2 + 4
    f2 = 5 * x ** 2 - 4
    return math.isqrt(f1) ** 2 == f1 or math.isqrt(f2) ** 2 == f2

def fibonacci_check(arr):
    result = []
    for number in arr:
        result.append("Yes" if is_fibonacci_number(number) else "No")
    return result


def task_6(input_file, output_file):
    n, nums = open_file(input_file)
    inputs = str(n) + '\n' + ''.join(nums)
    result = '\n'.join(fibonacci_check(nums))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(fibonacci_check, nums)


if __name__ == '__main__':
    task_6(PATH_INPUT, PATH_OUTPUT)
