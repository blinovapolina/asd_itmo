import unittest
import datetime

from lab6.task_2.src.lab6_2 import manage_phonebook


class TestManagePhonebook(unittest.TestCase):
    def test1_should_manage_phonebook(self):
        # Given
        commands = ['add 911 police', 'add 76213 Mom', 'add 17239 Bob', 'find 76213', 'find 910', 'find 911',
                    'del 910', 'del 911', 'find 911', 'find 76213', 'add 76213 daddy', 'find 76213']
        expected_time = datetime.timedelta(2)
        expected_result = ['Mom', 'not found', 'police', 'not found', 'Mom', 'daddy']

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = manage_phonebook(commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test2_should_manage_phonebook(self):
        # Given
        commands = ['find 3839442', 'add 123456 me', 'add 0 granny', 'find 0', 'find 123456', 'del 0', 'del 0', 'find 0']
        expected_time = datetime.timedelta(2)
        expected_result = ['not found', 'granny', 'me', 'not found']

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        result = manage_phonebook(commands)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
