import unittest
import datetime

from lab4.task_4.src.lab4_4 import check_brackets


class TestCheckBrackets(unittest.TestCase):
        def test1_should_check_brackets(self):
            # Given
            brackets_given = '[]'
            expected_time = datetime.timedelta(5)
            expected_result = 'Success'

            # When
            start_time = datetime.datetime.now()  # Запускаем счётчик времени
            result = check_brackets(brackets_given)
            finish_time = datetime.datetime.now()  # Измеряем время конца работы
            result_time = finish_time - start_time

            # Then
            self.assertEqual(result, expected_result)
            self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

        def test2_should_scheck_brackets(self):
            # Given
            brackets_given = '{}[]'
            expected_time = datetime.timedelta(5)
            expected_result = 'Success'

            # When
            start_time = datetime.datetime.now()  # Запускаем счётчик времени
            result = check_brackets(brackets_given)
            finish_time = datetime.datetime.now()  # Измеряем время конца работы
            result_time = finish_time - start_time

            # Then
            self.assertEqual(result, expected_result)
            self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

        def test3_should_check_brackets(self):
            # Given
            brackets_given = '[()]'
            expected_time = datetime.timedelta(5)
            expected_result = 'Success'

            # When
            start_time = datetime.datetime.now()  # Запускаем счётчик времени
            result = check_brackets(brackets_given)
            finish_time = datetime.datetime.now()  # Измеряем время конца работы
            result_time = finish_time - start_time

            # Then
            self.assertEqual(result, expected_result)
            self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

        def test4_should_check_brackets(self):
            # Given
            brackets_given = '(())'
            expected_time = datetime.timedelta(5)
            expected_result = 'Success'

            # When
            start_time = datetime.datetime.now()  # Запускаем счётчик времени
            result = check_brackets(brackets_given)
            finish_time = datetime.datetime.now()  # Измеряем время конца работы
            result_time = finish_time - start_time

            # Then
            self.assertEqual(result, expected_result)
            self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

        def test5_should_check_brackets(self):
            # Given
            brackets_given = '{'
            expected_time = datetime.timedelta(5)
            expected_result = 1

            # When
            start_time = datetime.datetime.now()  # Запускаем счётчик времени
            result = check_brackets(brackets_given)
            finish_time = datetime.datetime.now()  # Измеряем время конца работы
            result_time = finish_time - start_time

            # Then
            self.assertEqual(result, expected_result)
            self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

        def test6_should_check_brackets(self):
            # Given
            brackets_given = '{[}'
            expected_time = datetime.timedelta(5)
            expected_result = 3

            # When
            start_time = datetime.datetime.now()  # Запускаем счётчик времени
            result = check_brackets(brackets_given)
            finish_time = datetime.datetime.now()  # Измеряем время конца работы
            result_time = finish_time - start_time

            # Then
            self.assertEqual(result, expected_result)
            self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

        def test7_should_check_brackets(self):
            # Given
            brackets_given = 'foo(bar);'
            expected_time = datetime.timedelta(5)
            expected_result = 'Success'

            # When
            start_time = datetime.datetime.now()  # Запускаем счётчик времени
            result = check_brackets(brackets_given)
            finish_time = datetime.datetime.now()  # Измеряем время конца работы
            result_time = finish_time - start_time

            # Then
            self.assertEqual(result, expected_result)
            self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")

        def test8_should_check_brackets(self):
            # Given
            brackets_given = 'foo(bar[i);'
            expected_time = datetime.timedelta(5)
            expected_result = 10

            # When
            start_time = datetime.datetime.now()  # Запускаем счётчик времени
            result = check_brackets(brackets_given)
            finish_time = datetime.datetime.now()  # Измеряем время конца работы
            result_time = finish_time - start_time

            # Then
            self.assertEqual(result, expected_result)
            self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()
