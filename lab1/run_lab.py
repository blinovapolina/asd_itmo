import os
import sys

from lab1.task_1.src.lab1_1 import task_1 as task1_1
from lab1.task_2.src.lab1_2 import task_2 as task1_2
from lab1.task_3.src.lab1_3 import task_3 as task1_3
from lab1.task_5.src.lab1_5 import task_5 as task1_5
from lab1.task_6.src.lab1_6 import task_6 as task1_6
from lab1.task_10.src.lab1_10 import task_10 as task1_10


# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task1_1, [path+"/task_1/txtf/input.txt"]),
        "Задание №2": (task1_2, [path+"/task_2/txtf/input.txt"]),
        "Задание №3": (task1_3, [path+"/task_3/txtf/input.txt"]),
        "Задание №5": (task1_5, [path+"/task_5/txtf/input.txt"]),
        "Задание №6": (task1_6, [path + "/task_6/txtf/input.txt"]),
        "Задание №10": (task1_10, [path+"/task_10/txtf/input.txt"]),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('-' * 10 + '\n' + task_name + '\n' + '-' * 10)
        for input_file in inputs:
            output_file = input_file.replace("input", "output")
            task_func(input_file, output_file)
            print()


if __name__ == "__main__":
    main()
