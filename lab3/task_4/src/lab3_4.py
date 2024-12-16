from lab3.utils import open_file, write_file, measuring, print_input_output


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def count_intervals(p, intervals, dots):
    nums = [0] * p
    for i in range(p):
        for interval in intervals:
            if interval[0] < dots[i] < interval[-1]:
                nums[i] += 1
    return nums


def task_4(input_file, output_file):
    s, p, intervals, dots = open_file(input_file)
    inputs = (str(s) + ' ' + str(p) + '\n' + "\n".join(" ".join(map(str, interval)) for interval in intervals) +
              '\n' + " ".join(map(str, dots)))
    result = count_intervals(p, intervals, dots)
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=' '.join(map(str, result)))
    measuring(count_intervals, p, intervals, dots)


if __name__ == '__main__':
    task_4(PATH_INPUT, PATH_OUTPUT)
