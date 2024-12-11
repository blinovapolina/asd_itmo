from lab6.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def fibonacci_check(n, data):
    result = []
    s = set()

    for i in range(n):
        line = data[i].split()
        operation = line[0]
        x = int(line[1])

        if operation == 'A':
            s.add(x)
        elif operation == 'D':
            s.discard(x)
        elif operation == '?':
            if x in s:
                result.append('Y')
            else:
                result.append('N')

    return result


def task_1(input_file, output_file):
    n, commands = open_file(input_file)
    inputs = (str(n) + "\n" + "".join(commands))
    result = '\n'.join(fibonacci_check(n, commands))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(fibonacci_check, n, commands)


if __name__ == '__main__':
    task_1(PATH_INPUT, PATH_OUTPUT)
