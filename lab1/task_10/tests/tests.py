import unittest
import datetime

from lab1.task_10.src.lab1_10 import palindrom


class TestPalindrome(unittest.TestCase):
    def test1_should_make_palindrome(self):
        # Given
        letters = ['A', 'A', 'B']
        expected_time = datetime.timedelta(1)
        expected_result = 'ABA'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = palindrom(letters)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_make_palindrome(self):
        # Given
        letters = ['Q', 'A', 'Z', 'Q', 'A', 'Z']
        expected_time = datetime.timedelta(1)
        expected_result = 'AQZZQA'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = palindrom(letters)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test3_should_make_palindrome(self):
        # Given
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        expected_time = datetime.timedelta(1)
        expected_result = 'A'

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = palindrom(letters)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
