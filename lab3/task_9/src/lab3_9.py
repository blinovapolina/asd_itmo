import math
from lab3.utils import open_file, write_file, measuring, print_input_output
from lab3.task_1.src.lab3_1_1 import randomized_quicksort


PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def min_enum(points_arr, length_points):
    min_dist = float('inf')
    for i in range(length_points):
        for j in range(i + 1, length_points):
            min_dist = min(min_dist, distance(points_arr[i], points_arr[j]))
    return min_dist


def closest_pair(points_arr):
    length_points = len(points_arr)
    if length_points <= 3:
        return min_enum(points_arr, length_points)

    randomized_quicksort(points_arr, 0, len(points_arr) - 1)

    mid = length_points // 2
    min_dist = min(closest_pair(points_arr[:mid]), closest_pair(points_arr[mid:]))

    near_line = list()
    for i in range(0, length_points - 1):
        if abs(points_arr[i][0] - points_arr[mid][0]) < min_dist:
            near_line.append(points_arr[i])
    result = min(min_dist, min_enum(near_line, len(near_line)))

    return result


def task_9(input_file, output_file):
    n, points = open_file(input_file)
    inputs = (str(n) + '\n' + "\n".join(" ".join(map(str, points_el)) for points_el in points))
    result = f'{closest_pair(points):.5}'
    write_file(result, output_file)
    print_input_output(inputs=inputs, result=result)
    measuring(closest_pair, points)


if __name__ == '__main__':
    task_9(PATH_INPUT, PATH_OUTPUT)
