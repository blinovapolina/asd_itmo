import unittest
import datetime
import random
from lab5.task_7.src.lab5_7 import heap_sort


class TestHeapSort(unittest.TestCase):
    def test_should_sort_small_list(self):
        # Given
        small_size = 1000
        unsorted_list = [random.randint(-10 ** 9, 10 ** 9) for _ in range(small_size)]
        expected_time = datetime.timedelta(2)
        expected_result = sorted(unsorted_list, reverse=True)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = heap_sort(len(unsorted_list), unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_medium_list(self):
        # Given
        medium_size = 10 ** 3
        unsorted_list = [random.randint(10 ** 3, 10 ** 9) for _ in range(medium_size)]
        expected_time = datetime.timedelta(2)
        expected_result = sorted(unsorted_list, reverse=True)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = heap_sort(len(unsorted_list), unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_list(self):
        # Given
        large_size = 10 ** 5
        unsorted_list = [random.randint(1, 10 ** 9) for _ in range(large_size)]
        expected_time = datetime.timedelta(2)
        expected_result = sorted(unsorted_list, reverse=True)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = heap_sort(len(unsorted_list), unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
