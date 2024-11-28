import os
import sys

from lab2.task_1.src.lab2_1 import task_1 as task2_1
from lab2.task_2.src.lab2_2 import task_2 as task2_2
from lab2.task_3.src.lab2_3 import task_3 as task2_3
from lab2.task_4.src.lab2_4 import task_4 as task2_4
from lab2.task_5.src.lab2_5 import task_5 as task2_5
from lab2.task_10.src.lab2_10 import task_10 as task2_10


# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task2_1, [path+"/task_1/txtf/input.txt"]),
        "Задание №2": (task2_2, [path+"/task_2/txtf/input.txt"]),
        "Задание №3": (task2_3, [path+"/task_3/txtf/input.txt"]),
        "Задание №4": (task2_4, [path+"/task_4/txtf/input.txt"]),
        "Задание №5": (task2_5, [path+"/task_5/txtf/input.txt"]),
        "Задание №10": (task2_10, [path+"/task_10/txtf/input.txt"]),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('-' * 10 + '\n' + task_name + '\n' + '-' * 10)
        for input_file in inputs:
            output_file = input_file.replace("input", "output")
            task_func(input_file, output_file)
            print()


if __name__ == "__main__":
    main()
