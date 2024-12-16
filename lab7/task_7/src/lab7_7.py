from lab7.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def match_pattern(pattern, string):
    n, m = len(string), len(pattern)

    table = [[False] * (m + 1) for _ in range(n + 1)]
    table[0][0] = True

    for j in range(1, m + 1):
        if pattern[j - 1] == '*':
            table[0][j] = table[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[j - 1] == '?' or pattern[j - 1] == string[i - 1]:
                table[i][j] = table[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                table[i][j] = table[i - 1][j] or table[i][j - 1]

    return "YES" if table[n][m] else "NO"


def task_7(input_file, output_file):
    pattern, string = open_file(input_file)
    inputs = str(pattern) + '\n' + str(string)
    result = str(match_pattern(pattern, string))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(match_pattern, pattern, string)


if __name__ == '__main__':
    task_7(PATH_INPUT, PATH_OUTPUT)
