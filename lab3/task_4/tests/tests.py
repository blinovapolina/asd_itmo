import unittest
import datetime
from lab3.task_4.src.lab3_4 import count_intervals


class TestMergeSortCount(unittest.TestCase):
    def test1_should_sort_given_list(self):
        # Given
        s, p = 2, 3
        given_intervals = [[0, 5], [7, 10]]
        given_dots = [1, 6, 11]
        expected_time = datetime.timedelta(2)
        expected_result = [1, 0, 0]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = count_intervals(s, p, given_intervals, given_dots)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_sort_given_list(self):
        # Given
        s, p = 1, 3
        given_intervals = [[-10, 10]]
        given_dots = [-100, 100, 0]
        expected_time = datetime.timedelta(2)
        expected_result = [0, 0, 1]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = count_intervals(s, p, given_intervals, given_dots)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test3_should_sort_given_list(self):
        # Given
        s, p = 3, 2
        given_intervals = [[0, 5], [-3, 2], [7, 10]]
        given_dots = [1, 6]
        expected_time = datetime.timedelta(2)
        expected_result = [2, 0]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = count_intervals(s, p, given_intervals, given_dots)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
