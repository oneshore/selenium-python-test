import unittest

class TestMath(unittest.TestCase):
	def test_sanity(self):
		"""
		I'm testing the bounds of reality
		"""
		self.assertTrue(False)

	def test_addition(self):
		"""
		I'm testing addition
		"""
		self.assertEqual(1+1, 2)


if __name__ == "__main__":
	unittest.main()
