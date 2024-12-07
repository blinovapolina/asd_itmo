import unittest
import datetime
from lab3.task_2.src.lab3_2 import anti_qsort


class TestMergeSortCount(unittest.TestCase):
    def test_should_sort_given_list(self):
        # Given
        given_input = 3
        expected_time = datetime.timedelta(2)
        expected_result = [1, 3, 2]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = anti_qsort(given_input)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
