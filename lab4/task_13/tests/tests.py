import unittest
import datetime

from lab4.task_13.src.lab4_13_1 import result_f as stack


class TestStack(unittest.TestCase):
    def test1_stack(self):
        # Given
        nums = [1, 2, 3]
        expected_time = datetime.timedelta(2)
        expected_result = "Стек пуст: True\n1\n2, 1\n3, 2, 1\nИзвлечён элемент: 3\n2, 1\nСтек пуст: False\n"

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = stack('', nums)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
