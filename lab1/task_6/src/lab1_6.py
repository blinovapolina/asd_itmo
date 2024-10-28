from asd_itmo.utils import open_file, write_file


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def bubble_sort(n, A):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


def task_6():
    n, nums = open_file(PATH_INPUT)
    if 1 <= n <= 10 ** 3 and all([abs(n) <= 10 ** 9 for x in nums]):
        write_file(bubble_sort(n, nums), PATH_OUTPUT)
    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_6()


