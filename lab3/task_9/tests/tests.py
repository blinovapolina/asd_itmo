import unittest
import datetime
from lab3.task_9.src.lab3_9 import closest_pair


class TestClosestPair(unittest.TestCase):
    def test1_should_find_closest_pair(self):
        # Given
        given_points = [[0, 0], [3, 4]]
        expected_time = datetime.timedelta(10)
        expected_result = 5.0

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = closest_pair(given_points)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_find_closest_pair(self):
        # Given
        given_points = [[7, 7], [1, 100], [4, 8], [7, 7]]
        expected_time = datetime.timedelta(10)
        expected_result = 0.0

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = closest_pair(given_points)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test3_should_find_closest_pair(self):
        # Given
        given_points = [[4, 4], [-2, -2], [-3, -4], [-1, 3], [2, 3], [-4, 0],
                        [1, 1], [-1, -1], [3, -1], [-4, 2], [-2, 4]]
        expected_time = datetime.timedelta(10)
        expected_result = 1.4142

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = float(f'{closest_pair(given_points):.5}')
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
