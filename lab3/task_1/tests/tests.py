import unittest
import datetime

from lab3.task_1.src.lab3_1_1 import randomized_quicksort as sort_1
from lab3.task_1.src.lab3_1_2 import randomized_quicksort as sort_2


class TestQuickSort(unittest.TestCase):
    def test1_should_sort_given_list(self):
        # Given
        unsorted_list = [2, 3, 9, 2, 2]
        expected_time = datetime.timedelta(2)
        expected_result = [2, 2, 2, 3, 9]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = sort_1(unsorted_list, 0, len(unsorted_list) - 1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_sort_given_list(self):
        # Given
        unsorted_list = [2, 3, 9, 2, 2]
        expected_time = datetime.timedelta(2)
        expected_result = [2, 2, 2, 3, 9]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = sort_2(unsorted_list, 0, len(unsorted_list) - 1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
