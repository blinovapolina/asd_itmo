# Задание №6 по варианту  : `Очередь с минимумом`
Студентка ИТМО,  Блинова Полина Вячеславовна 465232

## Вариант 3

## Задание 
Реализуйте работу очереди. В дополнение к стандартным операциям очереди,
необходимо также отвечать на запрос о минимальном элементе из тех, которые
сейчас находится в очереди. Для каждой операции запроса минимального элемен-
та выведите ее результат.
На вход программе подаются строки, содержащие команды. Каждая строка
содержит одну команду. Команда – это либо «+ N », либо «–», либо «?». Команда
«+ N » означает добавление в очередь числа N , по модулю не превышающего 109.
Команда «–» означает изъятие элемента из очереди. Команда «?» означает запрос
на поиск минимального элемента в очереди.

## Input / Output

| Input | Output |
| ----- | ------ |
|7 <br/>+1 <br/> ?<br/> +10 <br/> ?<br/> -<br/> ?<br/> - | 1<br/>1<br/>10     |


## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/blinovapolina/asd_itmo.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd asd_itmo/lab4
   ```
3. Запустите программу:
   ```bash
   python task_6/src/lab4_6.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    python -m unittest -v lab4.task_6.tests.tests
```