import unittest

import run_tasks

class TestCeleryMethods(unittest.TestCase):

    def test_n1(self):
        self.assertEqual(run_tasks.func_run_tasks(), 0)

    def test_n1_1(self):
        self.assertEqual(run_tasks.func_run_tasks(), 1)

if __name__ == '__main__':
    unittest.main()