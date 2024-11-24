import unittest
import datetime
import random
from lab2.task_2.src.lab2_2 import merge_sort_output


class TestMergeSortOutput(unittest.TestCase):
    def test_should_sort_small_list(self):
        # Given
        small_size = 1000
        unsorted_list = [random.randint(-10 ** 9, 10 ** 9) for _ in range(small_size)]
        expected_time = 2
        expected_result = sorted(unsorted_list)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = merge_sort_output(unsorted_list, len(unsorted_list) * [0], 0, len(unsorted_list) - 1, list())
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_medium_list(self):
        # Given
        medium_size = 10 ** 4
        unsorted_list = [random.randint(-10 ** 9, 10 ** 9) for _ in range(medium_size)]
        expected_time = 2
        expected_result = sorted(unsorted_list)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = merge_sort_output(unsorted_list, len(unsorted_list) * [0], 0, len(unsorted_list) - 1, list())
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_should_sort_large_list(self):
        # Given
        large_size = 10 ** 5
        unsorted_list = [random.randint(-10 ** 9, 10 ** 9) for _ in range(large_size)]
        expected_time = 2
        expected_result = sorted(unsorted_list)

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = merge_sort_output(unsorted_list, len(unsorted_list) * [0], 0, len(unsorted_list) - 1, list())
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
