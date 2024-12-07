from lab4.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def check_brackets(data):
    stack = []
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for i, symb in enumerate(data, start=1):
        if symb in "([{":
            stack.append((symb, i))
        elif symb in ")]}":
            if not stack or stack[-1][0] != bracket_pairs[symb]:
                return i
            stack.pop()

    if stack:
        return stack[0][1]

    return "Success"


def task_4(input_file, output_file):
    s = open_file(input_file)
    inputs = (str(s))
    result = str(check_brackets(s))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(check_brackets, s)


if __name__ == '__main__':
    task_4(PATH_INPUT, PATH_OUTPUT)
