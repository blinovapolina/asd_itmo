import unittest
import datetime

from lab4.task_1.src.lab4_1 import stack_commands


class TestMergeSortCount(unittest.TestCase):
    def test1_should_sort_given_list(self):
        # Given
        commands = ['+ 1', '+ 10', '-', '+ 2', '+ 1234', '-']
        expected_time = datetime.timedelta(2)
        expected_result = [10, 1234]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = stack_commands(commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time
        print("Тест.Итоговое время алгоритма:", result_time)

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
