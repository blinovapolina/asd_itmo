import time

start = time.perf_counter()


def main():
    file_output = open('output.txt', 'w')

    def calc_fib(n):
        if n <= 1:
            return n

        return calc_fib(n - 1) + calc_fib(n - 2)

    with open('input.txt', 'r') as file:
        f = file.readline()
        n = int(f)
        if 0 <= n <= 45:
            res = calc_fib(n)
            file_output.write(str(res))
        else:
            print('Введите другое число')

    file_output.close()


if __name__ == '__main__':
    main()


finish = time.perf_counter()
print('Время работы: ' + str(finish - start))
