from lab4.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


class Queue:
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def add_mid(self, value):
        if len(self.queue) % 2 == 0:
            middle = len(self.queue) // 2
        else:
            middle = len(self.queue) // 2 + 1

        self.queue.insert(middle, value)

    def remove(self):
        del_value = self.queue[0]
        self.queue.pop(0)
        return del_value


def queue_min(commands):
    queue = Queue()
    result = list()
    for command in commands:
        if command[0] == "+":
            queue.add(int(command.split()[1]))
        elif command[0] == "*":
            queue.add_mid(int(command.split()[1]))
        elif command[0] == '-':
            result.append(queue.remove())
    return result


def task_9(input_file, output_file):
    m, commands = open_file(input_file)
    inputs = (str(m) + "\n" + "\n".join(commands))
    result = '\n'.join(map(str, queue_min(commands)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(queue_min, commands)


if __name__ == '__main__':
    task_9(PATH_INPUT, PATH_OUTPUT)
