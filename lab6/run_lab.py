import os
import sys

from lab6.task_1.src.lab6_1 import task_1 as task6_1
from lab6.task_2.src.lab6_2 import task_2 as task6_2
from lab6.task_5.src.lab6_5 import task_5 as task6_5
from lab6.task_6.src.lab6_6 import task_6 as task6_6


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task6_1, [path + "/task_1/txtf/input.txt"]),
        "Задание №2": (task6_2, [path + "/task_2/txtf/input.txt"]),
        "Задание №5": (task6_5, [path+"/task_5/txtf/input.txt"]),
        "Задание №6": (task6_6, [path + "/task_6/txtf/input.txt"]),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('-' * 10 + '\n' + task_name + '\n' + '-' * 10)
        for input_file in inputs:
            output_file = input_file.replace("input", "output")
            task_func(input_file, output_file)
            print()


if __name__ == "__main__":
    main()
