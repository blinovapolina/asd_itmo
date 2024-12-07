import unittest
import datetime
from lab2.task_3.src.lab2_3 import merge_sort_count


class TestMergeSortCount(unittest.TestCase):
    def test_should_sort_given_list(self):
        # Given
        unsorted_list = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        expected_time = datetime.timedelta(2)
        expected_result = 17

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = merge_sort_count(unsorted_list, [0] * len(unsorted_list), 0, len(unsorted_list) - 1)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
