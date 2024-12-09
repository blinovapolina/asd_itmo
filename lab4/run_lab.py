import os
import sys

from lab4.task_1.src.lab4_1 import task_1 as task4_1
from lab4.task_4.src.lab4_4 import task_4 as task4_4
from lab4.task_6.src.lab4_6 import task_6 as task4_6
from lab4.task_8.src.lab4_8 import task_8 as task4_8
from lab4.task_4.src.lab4_4 import task_4 as task4_4
from lab4.task_9.src.lab4_9 import task_9 as task4_9
from lab4.task_13.src.lab4_13_1 import task_13_1 as task4_13_1
from lab4.task_13.src.lab4_13_2 import task_13_2 as task4_13_2


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    tasks = {
        "Задание №1": (task4_1, [path + "/task_1/txtf/input.txt"]),
        "Задание №4": (task4_4, [path+"/task_4/txtf/input.txt"]),
        "Задание №6": (task4_6, [path+"/task_6/txtf/input.txt"]),
        "Задание №8": (task4_8, [path + "/task_8/txtf/input.txt"]),
        "Задание №9": (task4_9, [path+"/task_9/txtf/input.txt"]),
        "Задание №13.1": (task4_13_1, [path + "/task_13/txtf/input1.txt"]),
        "Задание №13.2": (task4_13_2, [path + "/task_13/txtf/input2.txt"]),
    }

    for task_name, (task_func, inputs) in tasks.items():
        print('-' * 10 + '\n' + task_name + '\n' + '-' * 10)
        for input_file in inputs:
            output_file = input_file.replace("input", "output")
            task_func(input_file, output_file)
            print()


if __name__ == "__main__":
    main()
