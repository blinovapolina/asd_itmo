import time
import tracemalloc
from lab1.utils import open_file, write_file


PATH_INPUT = '../txtf/input_1.txt'
PATH_OUTPUT = '../txtf/output.txt'


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


def task_10():
    start = time.perf_counter()
    tracemalloc.start()
    n, letters = open_file(PATH_INPUT)
    if 1 <= n <= 100000:
        write_file(palindrom(letters), PATH_OUTPUT)
    else:
        print("Количество элементов не соответствует ограничениям")
    finish = time.perf_counter()
    print('Время работы: ' + str(finish - start))
    print('Память: ' + str(tracemalloc.get_traced_memory()[1] / 1024) + ' Кб')
    tracemalloc.stop()


if __name__ == "__main__":
    task_10()

