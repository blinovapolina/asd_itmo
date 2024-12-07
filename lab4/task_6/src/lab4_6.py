from collections import deque

from lab4.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def queue_min(commands):
    # queue = deque()
    # current_queue = list()
    # min_queue = list()
    #
    # for command in commands:
    #     if command == "+":
    #         queue.append(int(command.split("+")[1]))
    #     elif command == "-":
    #         if queue:
    #             if queue.popleft() == min_queue[0]:
    #                 min_queue.pop(0)
    #
    #     elif command == '?':
    #         if min_queue:
    #             current_queue.append(min_queue[0])
    #         else:
    #             current_queue.append('')
    queue = list()
    result = list()
    for command in commands:
        if command[0] == "+":
            queue.append(int(command.split()[1]))
        elif command[0] == "-":
            queue.pop(0)
        elif command[0] == '?':
            result.append(min(queue))
    return result


def task_6(input_file, output_file):
    m, commands = open_file(input_file)
    inputs = (str(m) + "\n" + "\n".join(commands))
    result = '\n'.join(map(str, queue_min(commands)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(queue_min, commands)


if __name__ == '__main__':
    task_6(PATH_INPUT, PATH_OUTPUT)