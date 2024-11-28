import unittest

from lab2.task_1.tests.test import TestMergeSort
from lab2.task_2.tests.test import TestMergeSortOutput
from lab2.task_3.tests.test import TestMergeSortCount
from lab2.task_4.tests.test import TestBinarySearch
from lab2.task_5.tests.test import TestMajority
from lab2.task_10.tests.test import TestMergeSort


def create_tests():
    """ Создаёт набор тестов, который будет запускать"""
    suite = unittest.TestSuite()
    for all_test_suit in unittest.defaultTestLoader.discover("/", "test.py"):
        for test_suite in all_test_suit:
            suite.addTests(test_suite)

    return suite


if __name__ == "__main__":
    unittest.main()