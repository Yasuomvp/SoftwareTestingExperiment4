import unittest

from test_workfunc import TestWorkFunc


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(TestWorkFunc))
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

