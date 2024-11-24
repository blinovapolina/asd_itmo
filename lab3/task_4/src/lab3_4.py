from asd_itmo.lab3.utils import open_file, write_file


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def count_interval(n, k, intervals, dots):
    result = [0] * k
    for ind in range(k):
        for interval in intervals:
            if interval[0] < dots[ind] and dots[ind] < interval[-1]:
                result[ind] += 1
    return result


def task_4():
    data = open_file(PATH_INPUT)
    s, p = map(int, data[0].split())
    intervals = [list(map(int, i.split())) for i in data[1:s + 1]]
    dots = list(map(int, data[s + 1].split()))
    write_file(count_interval(s, p, intervals, dots), PATH_OUTPUT)


def task_2():
    n, nums = open_file(PATH_INPUT)
    if 1 <= n <= 2 * (10 ** 4) and all([abs(n) <= 10 ** 9 for _ in nums]):
        res = list()
        merge_sort_output(nums, [0] * n, 0, n - 1, res)
        for num_line in res:
            write_file(num_line + "\n", PATH_OUTPUT)
        write_file(" ".join(map(str, nums)), PATH_OUTPUT)

    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_4()