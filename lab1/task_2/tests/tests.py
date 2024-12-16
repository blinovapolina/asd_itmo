import unittest
import datetime
import random

from lab1.task_2.src.lab1_2 import insertion_sort


class TestSort(unittest.TestCase):
    def test1_should_sort_given_list(self):
        # Given
        unsorted_list = [1, 8, 4, 2, 3, 7, 5, 6, 9, 0]
        expected_time = datetime.timedelta(1)
        expected_result = [1, 2, 2, 2, 3, 5, 5, 6, 9, 1], sorted(unsorted_list)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = insertion_sort(len(unsorted_list), unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
