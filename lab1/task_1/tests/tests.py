import unittest
import datetime
import random

from lab1.task_1.src.lab1_1 import insertion_sort


class TestSort(unittest.TestCase):
    def test1_should_sort_given_list(self):
        # Given
        unsorted_list = [31, 41, 59, 26, 41, 58]
        expected_time = datetime.timedelta(1)
        expected_result = sorted(unsorted_list)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = insertion_sort(len(unsorted_list), unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_small_list(self):
        # Given
        small_size = 1000
        unsorted_list = [random.randint(-10 ** 9, 10 ** 9) for _ in range(small_size)]
        expected_time = datetime.timedelta(2)
        expected_result = sorted(unsorted_list)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = insertion_sort(len(unsorted_list), unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_list(self):
        # Given
        medium_size = 10 ** 4
        unsorted_list = [random.randint(-10 ** 9, 10 ** 9) for _ in range(medium_size)]
        expected_time = datetime.timedelta(2)
        expected_result = sorted(unsorted_list)

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
