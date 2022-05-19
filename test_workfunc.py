from work import *
import unittest

class TestWorkFunc(unittest.TestCase):

    def testStatementCoverage(self):
        self.assertEqual(1,DoWork(4,6,9),msg="执行路径：1 2 3 4 5 6")

    def testDecisionCoverage(self):
        self.assertEqual(4.358898943540674,DoWork(5,4,9),msg="执行路径：1 2 3 4")
        self.assertEqual(1,DoWork(4,6,11),msg="执行路径：1 4 5 6")

    def testConditionCoverage(self):
        self.assertEqual(1,DoWork(4,6,9),msg="执行路径：1 2 3 4 5 6")
        self.assertRaises(UnboundLocalError,DoWork,2,4,11)        # 执行路径：1 4

    def testConditionDecisionCoverage(self):
        self.assertEqual(1,DoWork(4,6,9),msg="执行路径：1 2 3 4 5 6")
        self.assertRaises(UnboundLocalError,DoWork,2,4,11)        # 执行路径：1 4

    def testMultipleConditionCoverage(self):
        self.assertEqual(1,DoWork(4,6,9),msg="执行路径：1 2 3 4 5 6")
        self.assertEqual(2,DoWork(4,4,11),msg="执行路径：1 4 5 6")
        self.assertEqual(1,DoWork(2,6,9),msg="执行路径：1 4 5 6")
        self.assertRaises(UnboundLocalError,DoWork,2,4,11)         # 执行路径：1 4

    def testPathCoverage(self):
        self.assertEqual(1,DoWork(4,6,9),msg="执行路径：1 2 3 4 5 6")
        self.assertRaises(UnboundLocalError,DoWork,2,4,11)        # 执行路径：1 4
        self.assertEqual(2,DoWork(4,4,11),msg="执行路径：1 4 5 6")
        self.assertEqual(4.358898943540674,DoWork(5,4,9),msg="执行路径：1 2 3 4")

















