import unittest
import datetime

from lab5.task_4.src.lab5_4 import build_heap


class TestBuildHeap(unittest.TestCase):
    def test1_should_build_heap(self):
        # Given
        nums = [5, 4, 3, 2, 1]
        expected_time = datetime.timedelta(2)
        expected_result = [(1, 4), (0, 1), (1, 3)]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = build_heap(5, nums)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_build_heap(self):
        # Given
        nums = [1, 3, 2, 5, 4]
        expected_time = datetime.timedelta(2)
        expected_result = []

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = build_heap(5, nums)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
