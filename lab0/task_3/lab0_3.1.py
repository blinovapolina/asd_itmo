import time

start = time.perf_counter()


def main():
    file_output = open('output.txt', 'w')

    def calc_fib_last_digit(n):
        if n <= 1:
            return n

        num1, num2 = 0, 1
        for i in range(2, n + 1):
            num1, num2 = num2, (num1 + num2) % 10
        return num2

    with open('input.txt', 'r') as file:
        f = file.readline()
        n = int(f)
        if 0 <= n <= 10 ** 7:
            res = calc_fib_last_digit(n)
            file_output.write(str(res))
        else:
            print('Введите другое число')

    file_output.close()


if __name__ == '__main__':
    main()


finish = time.perf_counter()
print('Время работы: ' + str(finish - start))
