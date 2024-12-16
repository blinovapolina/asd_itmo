import unittest
import datetime

from lab7.task_7.src.lab7_7 import match_pattern


class TestMatchPattern(unittest.TestCase):
    def test1_should_match_pattern(self):
        # Given
        pattern = 'k?t*n'
        string = 'kitten'
        expected_time = datetime.timedelta(1)
        expected_result = 'YES'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = match_pattern(pattern, string)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_match_pattern(self):
        # Given
        pattern = 'k?t?n'
        string = 'kitten'
        expected_time = datetime.timedelta(1)
        expected_result = 'NO'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = match_pattern(pattern, string)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
