a, b = map(int, list(input().split(' ')))
if (-10) ** 9 <= a <= 10 ** 9 and (-10) ** 9 <= b <= 10 ** 9:
    print(a + b ** 2)
else:
    print('Введите другое число')