import unittest
import datetime

from lab6.task_1.src.lab6_1 import fibonacci_check


class TestSetCommands(unittest.TestCase):
    def test1_should_set_commands(self):
        # Given
        commands = ['A 2', 'A 5', 'A 3', '? 2', '? 4', 'A 2', 'D 2', '? 2']
        expected_time = datetime.timedelta(2)
        expected_result = ['Y', 'N', 'N']

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = fibonacci_check(8, commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
