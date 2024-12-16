from lab7.utils import open_file, write_file, measuring, print_input_output

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def longest_common_subsequence(n, a, m, b, l, c):
    table = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    table[i][j][k] = table[i - 1][j - 1][k - 1] + 1
                else:
                    table[i][j][k] = max(table[i - 1][j][k], table[i][j - 1][k], table[i][j][k - 1])

    return table[n][m][l]


def task_5(input_file, output_file):
    n, a_list, m, b_list, l, c_list = open_file(input_file)
    inputs = (str(n) + '\n' + ' '.join(map(str, a_list)) + '\n' + str(m) + '\n' + ' '.join(map(str, b_list))+
              '\n' + str(l) + '\n' + ' '.join(map(str, c_list)))
    result = str(longest_common_subsequence(n, a_list, m, b_list, l, c_list))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(longest_common_subsequence, n, a_list, m, b_list, l, c_list)


if __name__ == '__main__':
    task_5(PATH_INPUT, PATH_OUTPUT)
