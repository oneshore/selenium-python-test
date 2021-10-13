import unittest

class TestSubtraction(unittest.TestCase):
    def test_result_is_seven(self):
        """Check that subtraction works"""
        self.assertEqual(7, 8-1)
    def test_result_is_eight(self):
        """Check that subtraction still works"""
        self.assertEqual(8, 8-0)


if __name__ == "__main__":
    unittest.main()
