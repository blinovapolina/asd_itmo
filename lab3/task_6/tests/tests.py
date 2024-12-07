import unittest
import datetime
from lab3.task_6.src.lab3_6 import summa_ten_sort


class TestMergeSortCount(unittest.TestCase):
    def test_should_sort_given_list(self):
        # Given
        given_a = [7, 1, 4, 9]
        given_b = [2, 7, 8, 11]
        expected_time = datetime.timedelta(2)
        expected_result = 51

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = summa_ten_sort(given_a, given_b)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
