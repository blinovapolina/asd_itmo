import unittest
import datetime

from lab5.task_2.src.lab5_2 import find_tree_height, build_tree


class TestTreeHeight(unittest.TestCase):
    def test1_should_find_tree_height(self):
        # Given
        nums = [4, -1, 4, 1, 1]
        expected_time = datetime.timedelta(2)
        expected_result = 3

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        tree, root = build_tree(5, nums)
        result = find_tree_height(tree, root)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")


    def test2_should_find_tree_height(self):
        # Given
        nums = [-1, 0, 4, 0, 3]
        expected_time = datetime.timedelta(2)
        expected_result = 4

        # When
        start_time = datetime.datetime.now()  # Запускаем счётчик времени
        tree, root = build_tree(5, nums)
        result = find_tree_height(tree, root)
        finish_time = datetime.datetime.now()  # Измеряем время конца работы
        result_time = finish_time - start_time

        # Then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")



if __name__ == '__main__':
    unittest.main()
