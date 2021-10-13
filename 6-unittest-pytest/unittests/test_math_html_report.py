import unittest

class TestMath(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(1+1, 2)

	def test_subtraction(self):
		self.assertGreater(5-1, 3)

	def test_multiplication(self):
		self.assertEqual(10*10, 99)

	def test_division(self):
		self.assertAlmostEqual(10/3, 3, 0)

	def test_divide_by_zero(self):
		with self.assertRaises(ZeroDivisionError):
			2/0

if __name__ == '__main__':
	from HtmlTestRunner import HTMLTestRunner
	unittest.main(testRunner= HTMLTestRunner(output="htmlreports"))
