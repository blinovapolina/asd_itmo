import unittest
import datetime
from lab2.task_5.src.lab2_5 import majority


class TestMajority(unittest.TestCase):
    def test_should_sort_given_list(self):
        # Given
        unsorted_list = [2, 3, 9, 2, 2]
        expected_time = datetime.timedelta(2)
        expected_result = 1

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = majority(len(unsorted_list), unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
