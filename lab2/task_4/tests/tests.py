import unittest
import datetime
from lab2.task_4.src.lab2_4 import search_elements


class TestBinarySearch(unittest.TestCase):
    def test_should_given_large_list(self):
        # Given
        initial_list = [1, 5, 8, 12, 13]
        list_search = [8, 1, 23, 1, 11]
        expected_time = datetime.timedelta(2)
        expected_result = [2, 0, -1, 0, -1]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = search_elements(initial_list, list_search)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
