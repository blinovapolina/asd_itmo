file_output = open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab2/task_5/tests/output.txt", 'w')


def find_majority(list_arr, left_i, right_i):
    if left_i == right_i:
        return list_arr[left_i]

    middle_arr = (left_i + right_i) // 2
    left = find_majority(list_arr, left_i, middle_arr)
    right = find_majority(list_arr, middle_arr + 1, right_i)

    counter_left, counter_right = 0, 0
    for i in range(left_i, right_i + 1):
        if list_arr[i] == right:
            counter_right += 1
        elif list_arr[i] == left:
            counter_left += 1
    return left if counter_left > counter_right else right


def majority(list_arr):
    result = find_majority(list_arr, 0, len(list_arr) - 1)
    if result:
        if list_arr.count(result) > n / 2:
            return 1
    return 0


with open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab2/task_5/tests/input_1.txt", 'r') as f:
    file = f.readlines()
    n = int(file[0])
    if 1 <= n <= 10 ** 5:
        nums = list(map(int, list(file[1].split(' '))))
        if all([abs(n) <= 10 ** 9 for x in nums]):
            file_output.write(str(majority(nums)))
        else:
            print('Введите другое число')
    else:
        print('Неверный ввод данных')

file_output.close()

