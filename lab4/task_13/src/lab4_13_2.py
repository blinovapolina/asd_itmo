from lab4.utils import open_file, write_file, print_input_output

PATH_INPUT = '../txtf/input2.txt'
PATH_OUTPUT = '../txtf/output.txt'


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, max_size):
        self.first = None
        self.last = None
        self.size = 0
        self.max_size = max_size

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def enqueue(self, value):
        if self.isFull():
            return 'Очередь переполнена'
        new_node = Node(value)
        if self.last is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return 'Очередь пуста'
        dequeued_value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.size -= 1
        return dequeued_value

    def peek(self):
        if self.isEmpty():
            return None
        return self.first.value

    def queue_size(self):
        return self.size


def result_f(result, max_size, nums):
    queue = Queue(max_size)
    result += f'Очередь пуста: {queue.isEmpty()}\n'
    result += f'Добавление элементов в очередь...\n'
    for num in nums:
        queue.enqueue(num)
        result += f"Было добавлено: {num}\n"
        result += f"Последний элемент очереди: {queue.peek()}\n\n"

    result += f'Добавление элементов закончено\n'
    result += f"Размер очереди: {queue.queue_size()}\n"

    queue.dequeue()
    result += f"Был извлечён последний элемент\n"
    result += f"Размер очереди: {queue.queue_size()}\n"
    result += f"Последний элемент очереди: {queue.peek()}\n\n"
    return result


def task_13_2(input_file, output_file):
    data = open_file(input_file)
    max_size, nums = data[0], data[1:]
    inputs = str(max_size) + '\n' + ("\n".join(map(str, nums)))
    result = result_f('', max_size, nums)
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)


if __name__ == '__main__':
    task_13_2(PATH_INPUT, PATH_OUTPUT)

