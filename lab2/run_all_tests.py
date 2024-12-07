import unittest

from lab2.task_1.tests.tests import TestMergeSort
from lab2.task_2.tests.tests import TestMergeSortOutput
from lab2.task_3.tests.tests import TestMergeSortCount
from lab2.task_4.tests.tests import TestBinarySearch
from lab2.task_5.tests.tests import TestMajority
from lab2.task_10.tests.tests import TestMergeSort


def create_tests():
    """ Создаёт набор тестов, который будет запускать"""
    suite = unittest.TestSuite()
    for all_test_suit in unittest.defaultTestLoader.discover("/", "tests.py"):
        for test_suite in all_test_suit:
            suite.addTests(test_suite)

    return suite


if __name__ == "__main__":
    unittest.main()