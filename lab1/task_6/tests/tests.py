import unittest
import datetime
import random

from lab1.task_6.src.lab1_6 import bubble_sort


class TestSort(unittest.TestCase):
    def test1_should_sort_given_list(self):
        # Given
        unsorted_list = [5, 6, 9, 0, 4, 6, 5, 1]
        expected_time = datetime.timedelta(1)
        expected_result = sorted(unsorted_list)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = bubble_sort(len(unsorted_list), unsorted_list)
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
        result = bubble_sort(len(unsorted_list), unsorted_list)
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
        result = bubble_sort(len(unsorted_list), unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()

