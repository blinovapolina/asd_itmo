file_output = open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab2/task_4/tests/output.txt", 'w')


def binary_search(list_arr, number):
    left, right = 0, len(list_arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if list_arr[middle] == number:
            return middle
        elif list_arr[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return -1


with open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab2/task_4/tests/input.txt", 'r') as f:
    file = f.readlines()
    n = int(file[0])
    nums = list(map(int, list(file[1].split(' '))))
    k = int(file[2])
    list_search = list(map(int, list(file[3].split(' '))))
    if 1 <= n <= 10 ** 5 and 1 <= k <= 10 ** 5:
        nums = list(map(int, list(file[1].split(' '))))
        if all([abs(n) <= 10 ** 9 for x in nums]) and all([abs(n) <= 10 ** 9 for x in list_search]):
            result = [binary_search(nums, number) for number in list_search]
            file_output.write(' '.join(map(str, result)))
        else:
            print('Введите другое число')
    else:
        print('Неверный ввод данных')

file_output.close()

