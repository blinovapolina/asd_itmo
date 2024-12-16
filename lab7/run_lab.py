import os
import sys

from lab7.task_1.src.lab7_1 import task_1 as task7_1
from lab7.task_4.src.lab7_4 import task_4 as task7_4
from lab7.task_5.src.lab7_5 import task_5 as task7_5
from lab7.task_7.src.lab7_7 import task_7 as task7_7


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task7_1, [path + "/task_1/txtf/input.txt"]),
        "Задание №4": (task7_4, [path + "/task_4/txtf/input.txt"]),
        "Задание №5": (task7_5, [path+"/task_5/txtf/input.txt"]),
        "Задание №7": (task7_7, [path + "/task_7/txtf/input.txt"]),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('-' * 10 + '\n' + task_name + '\n' + '-' * 10)
        for input_file in inputs:
            output_file = input_file.replace("input", "output")
            task_func(input_file, output_file)
            print()


if __name__ == "__main__":
    main()
