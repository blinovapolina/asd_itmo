import os
import sys

from lab5.task_1.src.lab5_1 import task_1 as task5_1
from lab5.task_4.src.lab5_4 import task_4 as task5_4
from lab5.task_2.src.lab5_2 import task_2 as task5_2
from lab5.task_7.src.lab5_7 import task_7 as task5_7


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task5_1, [path + "/task_1/txtf/input.txt"]),
        "Задание №2": (task5_2, [path + "/task_2/txtf/input.txt"]),
        "Задание №4": (task5_4, [path+"/task_4/txtf/input.txt"]),
        "Задание №7": (task5_7, [path + "/task_7/txtf/input.txt"]),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('-' * 10 + '\n' + task_name + '\n' + '-' * 10)
        for input_file in inputs:
            output_file = input_file.replace("input", "output")
            task_func(input_file, output_file)
            print()


if __name__ == "__main__":
    main()
