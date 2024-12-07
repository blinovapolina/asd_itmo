import unittest
import datetime
from lab3.task_3.src.lab3_3 import pugalo_sort


class TestMergeSortCount(unittest.TestCase):
    def test1_should_sort_given_list(self):
        # Given
        n, k = 3, 2
        unsorted_list = [2, 1, 3]
        expected_time = datetime.timedelta(2)
        expected_result = "НЕТ"

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = pugalo_sort(n, k, unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_sort_given_list(self):
        # Given
        n, k = 5, 3
        unsorted_list = [1, 5, 3, 4, 1]
        expected_time = datetime.timedelta(2)
        expected_result = "ДА"

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = pugalo_sort(n, k, unsorted_list)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
