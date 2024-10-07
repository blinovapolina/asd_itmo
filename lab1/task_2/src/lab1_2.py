file_output = open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_2/tests/output.txt", 'w')


def insertion_sort(n, list_arr):
    index_result = [1]
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if list_arr[i] < list_arr[j]:
                list_arr[i], list_arr[j] = list_arr[j], list_arr[i]
                i, j = j, i
        index_result.append(i + 1)
    return index_result, list_arr


with open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_2/tests/input.txt", 'r') as f:
    file = f.readlines()
    n = int(file[0])
    if 1 <= n <= 10 ** 3:
        nums = list(map(int, list(file[1].split(' '))))
        if all([abs(n) <= 10 ** 9 for x in nums]):
            index_list, res = insertion_sort(n, nums)
            file_output.write(f"{' '.join(map(str, index_list))}\n")
            file_output.write(' '.join(map(str, res)))
        else:
            print('Введите другое число')
    else:
        print('Неверный ввод данных')

file_output.close()

