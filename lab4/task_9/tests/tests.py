import unittest
import datetime

from lab4.task_9.src.lab4_9 import queue_min


class TestQueue(unittest.TestCase):
    def test1_should_queue(self):
        # Given
        commands = ['+ 1', '+ 2', '-', '+ 3', '+ 4', '-', '-']
        expected_time = datetime.timedelta(2)
        expected_result = [1, 2, 3]

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = queue_min(commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
