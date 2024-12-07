import os
import sys

from lab3.task_1.src.lab3_1_1 import task_1_1 as task3_1_1
from lab3.task_1.src.lab3_1_2 import task_1_2 as task3_1_2
from lab3.task_2.src.lab3_2 import task_2 as task3_2
from lab3.task_3.src.lab3_3 import task_3 as task3_3
from lab3.task_4.src.lab3_4 import task_4 as task3_4
from lab3.task_6.src.lab3_6 import task_6 as task3_6
from lab3.task_9.src.lab3_9 import task_9 as task3_9


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1.1": (task3_1_1, [path+"/task_1/txtf/input.txt"]),
        "Задание №1.2": (task3_1_2, [path + "/task_1/txtf/input.txt"]),
        "Задание №2": (task3_2, [path+"/task_2/txtf/input.txt"]),
        "Задание №3": (task3_3, [path+"/task_3/txtf/input.txt"]),
        "Задание №4": (task3_4, [path+"/task_4/txtf/input.txt"]),
        "Задание №6": (task3_6, [path+"/task_6/txtf/input.txt"]),
        "Задание №9": (task3_9, [path+"/task_9/txtf/input.txt"]),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('-' * 10 + '\n' + task_name + '\n' + '-' * 10)
        for input_file in inputs:
            output_file = input_file.replace("input", "output")
            task_func(input_file, output_file)
            print()


if __name__ == "__main__":
    main()
