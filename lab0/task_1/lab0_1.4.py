file_output = open('output.txt', 'w')


with open('input.txt', 'r') as f:
    file = f.readline()
    a, b = map(int, list(file.split(' ')))
    if (-10) ** 9 <= a <= 10 ** 9 and (-10) ** 9 <= b <= 10 ** 9:
        file_output.write(str(a + b ** 2))


file_output.close()