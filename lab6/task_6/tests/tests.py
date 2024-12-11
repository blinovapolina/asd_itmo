import unittest
import datetime

from lab6.task_6.src.lab6_6 import fibonacci_check


class TestFibonacciChecks(unittest.TestCase):
    def test1_should_fibonacci_check(self):
        # Given
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        expected_time = datetime.timedelta(2)
        expected_result = ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = fibonacci_check(nums)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
