from lab4.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def stack_commands(commands):
    stack = list()
    deleted_el = list()
    for command in commands:
        if command[0] == '+':
            stack.append(int(command.split('+')[1]))
        elif command == '-':
            element = stack.pop()
            deleted_el.append(element)
    return deleted_el


def task_1(input_file, output_file):
    m, commands = open_file(input_file)
    inputs = (str(m) + "\n" + "\n".join(commands))
    result = '\n'.join(map(str, stack_commands(commands)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(stack_commands, commands)


if __name__ == '__main__':
    task_1(PATH_INPUT, PATH_OUTPUT)


