file_output = open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_3/tests/output.txt", 'w')


def insertion_sort(n, list_arr):
    for i in range(1, n):
        key = list_arr[i]
        j = i - 1
        while j >= 0 and key > list_arr[j]:
            list_arr[j + 1] = list_arr[j]
            j -= 1
        list_arr[j + 1] = key
    return list_arr


with open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_3/tests/input.txt", 'r') as f:
    file = f.readlines()
    n = int(file[0])
    if 1 <= n <= 10 ** 3:
        nums = list(map(int, list(file[1].split(' '))))
        if all([abs(n) <= 10 ** 9 for x in nums]):
            file_output.write(' '.join(map(str, insertion_sort(n, nums))))
        else:
            print('Введите другое число')
    else:
        print('Неверный ввод данных')

file_output.close()
