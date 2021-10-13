import unittest
from addition_tests import AdditionTest
from test_subtraction import TestSubtraction

def suite():
	suite = unittest.TestSuite()
	suite.addTest(TestSubtraction('test_result_is_seven'))
	suite.addTest(AdditionTest('test_one_plus_one'))
	return suite

if __name__ == "__main__":
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite())
