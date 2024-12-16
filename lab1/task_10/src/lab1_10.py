from lab1.utils import open_file, write_file, print_input_output, measuring


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


def task_10(input_file, output_file):
    n, letters = open_file(input_file)
    inputs = (str(n) + "\n" + " ".join(map(str, letters)))
    result = ' '.join(map(str, palindrom(letters)))
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(palindrom, letters)


if __name__ == '__main__':
    task_10(PATH_INPUT, PATH_OUTPUT)
