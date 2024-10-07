import time
import tracemalloc

start = time.perf_counter()
tracemalloc.start()

file_output = open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_10/tests/output.txt", 'w')


def palindrom(str_in):
    if len(str_in) == len(set(str_in)):
        return sorted(list(str_in))[0]
    else:
        dict_nechet_letters = dict()
        chet_letters = ''
        set_list = list(set(str_in))

        for letter in sorted(set_list):
            counter = str_in.count(letter)
            if counter % 2 == 0:
                chet_letters += letter * (counter // 2)
            else:
                dict_nechet_letters[letter] = counter

        result = list()
        if dict_nechet_letters:
            for letter in dict_nechet_letters:
                res = chet_letters + letter * dict_nechet_letters[letter] + chet_letters[::-1]
                if result:
                    if len(res) > len(result[0]):
                        result = list()
                    elif len(res) < len(result[0]):
                        continue
                result.append(res)
            return min(result)
        return chet_letters + chet_letters[::-1]


with open("C:/Users/Slawa/Desktop/Uni/asd_itmo/lab1/task_10/tests/input_3.txt", 'r') as f:
    file = f.readlines()
    n = int(file[0])
    if 1 <= n <= 100000:
        letters = list(file[1])
        result = palindrom(letters)
        file_output.write(result)
    else:
        print('Неверный ввод данных')

file_output.close()
finish = time.perf_counter()
print('Время работы: ' + str(finish - start))
print('Память: ' + str(tracemalloc.get_traced_memory()[1]/1024) + ' Кб')
tracemalloc.stop()

