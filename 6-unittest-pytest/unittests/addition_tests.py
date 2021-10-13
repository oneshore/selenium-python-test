import unittest

class AdditionTest(unittest.TestCase):
	def test_one_plus_one(self):
		""" check that addition works"""
		self.assertEqual(1+1, 2)

	def test_two_plus_two(self):
		""" check that addition still works """
		self.assertEqual(2+2, 4)
