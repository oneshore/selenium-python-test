import unittest

def square(n):
	return n*n

class Test(unittest.TestCase):
	def test_square_of_two(self):
		self.assertEqual(square(2), 4)

	def test_square_of_three(self):
		self.assertEqual(square(3), 9)

	def test_square_fails_with_text(self):
		self.assertEqual(square("four", 16))
