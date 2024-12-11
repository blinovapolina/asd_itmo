import unittest
import datetime

from lab6.task_5.src.lab6_5 import process_elections


class TestProcessElections(unittest.TestCase):
    def test1_should_process_election(self):
        # Given
        candidates = ['McCain 10', 'McCain 5', 'Obama 9', 'Obama 8', 'McCain 1']
        expected_time = datetime.timedelta(2)
        expected_result = ['McCain 16', 'Obama 17']

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = process_elections(candidates)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_process_election(self):
        # Given
        candidates = ['ivanov 100', 'ivanov 500', 'ivanov 300', 'petr 70', 'tourist 1', 'tourist 2']
        expected_time = datetime.timedelta(2)
        expected_result = ['ivanov 900', 'petr 70', 'tourist 3']

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = process_elections(candidates)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test3_should_process_election(self):
        # Given
        candidates = ['bur 1']
        expected_time = datetime.timedelta(2)
        expected_result = ['bur 1']

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = process_elections(candidates)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
