from lab4.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def postfix_calculate(expression):
    stack = []
    actions = ['+', '-', '*', '/']
    for symbol in expression.split():
        if symbol not in actions:
            stack.append(int(symbol))
        else:
            b = stack.pop()
            a = stack.pop()
            if symbol == '+':
                stack.append(a + b)
            elif symbol == '-':
                stack.append(a - b)
            elif symbol == '*':
                stack.append(a * b)
            elif symbol == '/':
                stack.append(int(a / b))
    return stack[0]


def task_8(input_file, output_file):
    m, commands = open_file(input_file)
    inputs = (str(m) + "\n" + "".join(commands))
    result = str(postfix_calculate(commands))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(postfix_calculate, commands)


if __name__ == '__main__':
    task_8(PATH_INPUT, PATH_OUTPUT)
