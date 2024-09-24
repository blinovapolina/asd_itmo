import time

start = time.perf_counter()

file_output = open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_6/tests/output.txt", 'w')


def bubble_sort(n, A):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


with open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_6/tests/input.txt", 'r') as f:
    file = f.readlines()
    n = int(file[0])
    if 1 <= n <= 10 ** 3:
        nums = list(map(int, list(file[1].split(' '))))
        if all([abs(n) <= 10 ** 9 for x in nums]):
            file_output.write(' '.join(map(str, bubble_sort(n, nums))))
        else:
            print('Введите другое число')
    else:
        print('Неверный ввод данных')

file_output.close()

finish = time.perf_counter()
print('Время работы: ' + str(finish - start))

