"""Test for 6-max_integer function module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a test class for the max_integer"""
    def test_max_integer(self):
        """This is a test function"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -4]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, ["a", "b", 4])
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertRaises(TypeError, max_integer, 7)
        self.assertEqual(max_integer([7.1, 4.0, 3.1]), 7.1)
        self.assertEqual(max_integer([7.1, 4, 3]), 7.1)
        self.assertEqual(max_integer([1]), 1)
