file_output = open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab2/task_1/tests/output.txt", 'w')


def merge(left, right):
    list_merged = list()
    left_i = right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                list_merged.append(left[left_i])
                left_i += 1
            else:
                list_merged.append(right[right_i])
                right_i += 1

    while left_i < len(left):
        list_merged.append(left[left_i])
        left_i += 1

    while right_i < len(right):
        list_merged.append(right[right_i])
        right_i += 1

    return list_merged


def merge_sort(list_arr):
    if len(list_arr) <= 1:
        return list_arr

    middle = len(list_arr) // 2
    left_list = merge_sort(list_arr[:middle])
    right_list = merge_sort(list_arr[middle:])
    return merge(left_list, right_list)


with open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab2/task_1/tests/input.txt", 'r') as f:
    file = f.readlines()
    n = int(file[0])
    if 1 <= n <= 2 * (10 ** 4):
        nums = list(map(int, list(file[1].split(' '))))
        if all([abs(n) <= 10 ** 9 for x in nums]):
            file_output.write(' '.join(map(str, merge_sort(nums))))
        else:
            print('Введите другое число')
    else:
        print('Неверный ввод данных')

file_output.close()

