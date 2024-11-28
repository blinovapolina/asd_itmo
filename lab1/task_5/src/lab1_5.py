from lab1.utils import open_file, write_file


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def selection_sort(n, A):
    for i in range(n - 1):
        min_local = i
        for j in range(i + 1, n):
            if A[j] < A[min_local]:
                min_local = j
        A[i], A[min_local] = A[min_local], A[i]
    return A


def task_5():
    n, nums = open_file(PATH_INPUT)
    if 1 <= n <= 10 ** 3 and all([abs(n) <= 10 ** 9 for x in nums]):
        write_file(selection_sort(n, nums), PATH_OUTPUT)
    else:
        print("Число в массиве по модулю превосходит 10^9 или количество элементов не соответствует ограничениям")


if __name__ == "__main__":
    task_5()


