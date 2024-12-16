import unittest
import datetime

from lab7.task_5.src.lab7_5 import longest_common_subsequence


class TestCcommonSubsequence(unittest.TestCase):
    def test1_should_find_longest_common_subsequence(self):
        # Given
        n, m, l = 3, 3, 3
        a_list = [1, 2, 3]
        b_list = [2, 1, 3]
        c_list = [1, 3, 5]
        expected_time = datetime.timedelta(1)
        expected_result = 2

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = longest_common_subsequence(n, a_list, m, b_list, l, c_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_find_longest_common_subsequence(self):
        # Given
        n, m, l = 5, 7, 6
        a_list = [8, 3, 2, 1, 7]
        b_list = [8, 2, 1, 3, 8, 10, 7]
        c_list = [6, 8, 3, 1, 4, 7]
        expected_time = datetime.timedelta(1)
        expected_result = 3

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = longest_common_subsequence(n, a_list, m, b_list, l, c_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
