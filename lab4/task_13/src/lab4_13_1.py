from lab4.utils import open_file, write_file, print_input_output

PATH_INPUT = '../txtf/input1.txt'
PATH_OUTPUT = '../txtf/output.txt'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def display(self):
        if self.isEmpty():
            return
        current = self.top
        elements = list()
        while current:
            elements.append(current.data)
            current = current.next
        return ", ".join(map(str, elements))


def result_f(result, nums):
    stack = Stack()
    result += f'Стек пуст: {stack.isEmpty()}\n'
    for num in nums:
        stack.push(num)
        result += stack.display() + '\n'
    result += f'Извлечён элемент: {stack.pop()}\n'
    result += stack.display() + '\n'
    result += f'Стек пуст: {stack.isEmpty()}\n'
    return result

def task_13_1(input_file, output_file):
    nums = open_file(input_file)
    inputs = ("\n".join(map(str, nums)))
    result = result_f('', nums)
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)


if __name__ == '__main__':
    task_13_1(PATH_INPUT, PATH_OUTPUT)
