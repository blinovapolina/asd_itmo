# Задание №9 по варианту  : `Ближайшие точки`
Студентка ИТМО,  Блинова Полина Вячеславовна 465232

## Вариант 3

## Задание 
В этой задаче, ваша цель - найти пару ближайших точек среди данных n точек
(между собой). Это базовая задача вычислительной геометрии, которая находит
применение в компьютерном зрении, систем управления трафиком.
- Цель. Заданы n точек на поверхности, найти наименьшее расстояние между
двумя (разными) точками.

## Input / Output

| Input                                                             | Output                    |
|-------------------------------------------------------------------|---------------------------|
| + 1<br/>+ 2<br/>* 3<br/>-<br/>+ 4<br/>* 5<br/>-<br/>-<br/>-<br/>- | 1<br/>3<br/>2<br/>5<br/>4 |
| + 1<br/>+ 2<br/>-<br/>+ 3<br/>+ 4<br/>-<br/>-                     | 1<br/>2<br/>3             |


## Ограничения по времени и памяти

- Ограничение по времени. 10сек.
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
   python task_9/src/lab3_9.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    python -m unittest -v lab3.task_9.tests.tests
```