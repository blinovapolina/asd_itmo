file_output = open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_5/tests/output.txt", 'w')


def selection_sort(n, A):
    for i in range(n - 1):
        min_local = i
        for j in range(i + 1, n):
            if A[j] < A[min_local]:
                min_local = j
        A[i], A[min_local] = A[min_local], A[i]
    return A


with open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_5/tests/input.txt", 'r') as f:
    file = f.readlines()
    n = int(file[0])
    if 1 <= n <= 10 ** 3:
        nums = list(map(int, list(file[1].split(' '))))
        if all([abs(n) <= 10 ** 9 for x in nums]):
            file_output.write(' '.join(map(str, selection_sort(n, nums))))
        else:
            print('Введите другое число')
    else:
        print('Неверный ввод данных')

file_output.close()
