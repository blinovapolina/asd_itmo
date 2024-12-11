import unittest
import datetime

from lab4.task_8.src.lab4_8 import postfix_calculate


class TestMergeSortCount(unittest.TestCase):
    def test1_should_sort_given_list(self):
        # Given
        commands = '8 9 + 1 7 - *'
        expected_time = datetime.timedelta(2)
        expected_result = -102

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = postfix_calculate(commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_sort_given_list(self):
        # Given
        commands = '8 9 +'
        expected_time = datetime.timedelta(2)
        expected_result = 17

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = postfix_calculate(commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")



if __name__ == '__main__':
    unittest.main()
