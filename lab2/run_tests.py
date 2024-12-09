import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_all_tests():

    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(base_dir)


    test_files = [
        'lab2.task_1.tests.tests',
        'lab2.task_2.tests.tests',
        'lab2.task_3.tests.tests',
        'lab2.task_4.tests.tests',
        'lab2.task_5.tests.tests',
        'lab2.task_10.tests.tests',
    ]

    for test_file in test_files:
        try:
            print(f'======= RUNNING {".".join(test_file.split('.')[:2])} TESTS =======')
            suite = unittest.defaultTestLoader.loadTestsFromName(test_file)
            runner = unittest.TextTestRunner()
            runner.run(suite)
            print(f'======= RUNNING {".".join(test_file.split('.')[:2])} COMPLETED =======' + '\n')
        except ModuleNotFoundError as e:
            print(f"Ошибка при добавлении теста {test_file}: {e}")

if __name__ == "__main__":
    run_all_tests()