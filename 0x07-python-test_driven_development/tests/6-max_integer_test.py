#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger Unittest"""

    def test_max_integer(self):
        """Test max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]),  4)
        self.assertEqual(max_integer([1, 2, 50, 3, 4]),  50)
        self.assertEqual(max_integer([1]),  1)
        self.assertEqual(max_integer([]),  None)
        self.assertEqual(max_integer([-1, -3, -4, -5]),  -1)
        with self.assertRaises(TypeError):
            max_integer([-1, -323, -56, "inf"])
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
