import unittest

class TestMath(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(1+1, 2)

	def test_division(self):
		self.assertAlmostEqual(10/3, 3, 0)

	def test_subtraction(self):
		self.assertGreater(5-1, 3)

	def test_divide_by_zero(self):
		with self.assertRaises(ZeroDivisionError):
			a = 2
			b = 2
			print(a/b)


if __name__ == '__main__':
	unittest.main()
