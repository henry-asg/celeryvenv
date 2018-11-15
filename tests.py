import unittest

import run_tasks

class TestCeleryMethods(unittest.TestCase):

    def test_n1(self):
        self.assertEqual(run_tasks.func_run_tasks(), 0)

    def test_n1_1(self):
        self.assertEqual(run_tasks.func_run_tasks(), 1)

    def test_n1_2(self):
        self.assertEqual(run_tasks.func_run_tasks(), 2)

    # def test_n1_3(self):
    #     self.assertEqual(run_tasks.func_run_tasks(), 3)

if __name__ == '__main__':
    import xmlrunner
    # unittest.main(exit=False)
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))