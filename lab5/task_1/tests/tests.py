import unittest
import datetime

from lab5.task_1.src.lab5_1 import is_heap


class TestIsHeap(unittest.TestCase):
    def test1_should_is_heap(self):
        # Given
        nums = [1, 0, 1, 2, 0]
        expected_time = datetime.timedelta(2)
        expected_result = 'NO'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = is_heap(5, nums)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_is_heap(self):
        # Given
        nums = [1, 3, 2, 5, 4]
        expected_time = datetime.timedelta(2)
        expected_result = 'YES'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = is_heap(5, nums)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
