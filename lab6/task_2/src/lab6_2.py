from lab6.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def manage_phonebook(data):
    phonebook = {}
    result = []

    for query in data:
        command = query.split()[0]

        if command == 'add':
            phonebook[query.split()[1]] = query.split()[2]

        elif command == 'del':
            number = query.split()[1]
            if number in phonebook:
                del phonebook[number]

        elif command == 'find':
            number = query.split()[1]
            if number in phonebook:
                result.append(phonebook[number])
            else:
                result.append('not found')

    return result


def task_2(input_file, output_file):
    n, commands = open_file(input_file)
    inputs = (str(n) + "\n" + "".join(commands))
    result = '\n'.join(manage_phonebook(commands))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(manage_phonebook, commands)


if __name__ == '__main__':
    task_2(PATH_INPUT, PATH_OUTPUT)
