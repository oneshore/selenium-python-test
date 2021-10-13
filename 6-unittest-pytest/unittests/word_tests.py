import unittest

class WordTests(unittest.TestCase):

	def test_word_in_string(self):
		greeting = "Hi my name is Aaron"
		self.assertIn("Aaron", greeting)

	def test_word_in_list(self):
		names = ["Virang", "Dilip", "Ravi", "Udit", "Jeegna"]
		self.assertIn("Dilip", names)

	def test_word_slice(self):
		names = ["Aaron", "Miten", "Tejas"]
		with self.assertRaises(IndexError):
			names[2]

if __name__ == "__main__":
	unittest.main()
