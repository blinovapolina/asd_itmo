# Задание №1 по варианту  : `Улучшение Quick sort`
Студентка ИТМО,  Блинова Полина Вячеславовна 465232

## Вариант 3

## Задание 
Основное задание. Цель задачи - переделать данную реализацию рандо-
мизированного алгоритма быстрой сортировки, чтобы она работала быстро
даже с последовательностями, содержащими много одинаковых элементов.
Чтобы заставить алгоритм быстрой сортировки эффективно обрабатывать
последовательности с несколькими уникальными элементами, нужно заме-
нить двухстороннее разделение на трехстороннее (смотри в Лекции 3 слайд
17).

## Input / Output

| Input | Output |
| ----- | ------ |
| 5     | 2 2 2 3 9      |
| 2 3 9 2 2  |     |

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
   cd asd_itmo/lab3
   ```
3. Запустите программу:
   ```bash
   python task_1/src/lab3_1.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    python -m unittest -v lab3.task_1.tests.tests
```
