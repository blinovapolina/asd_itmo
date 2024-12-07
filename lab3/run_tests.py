import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_all_tests():
    suite = unittest.TestSuite()

    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(base_dir)


    test_files = [
        'lab3.task_1.tests.tests',
        'lab3.task_2.tests.tests',
        'lab3.task_3.tests.tests',
        'lab3.task_4.tests.tests',
        'lab3.task_6.tests.tests',
        'lab3.task_9.tests.tests',
    ]

    for test_file in test_files:
        try:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test_file))
        except ModuleNotFoundError as e:
            print(f"Ошибка при добавлении теста {test_file}: {e}")

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()