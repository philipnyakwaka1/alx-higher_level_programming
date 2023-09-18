"""Test module for class Rectangle"""


from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """This is a test class for class Rectangle"""

    def test_positives(self):
        """test for all positive integers"""

        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 3)

    def test_instance(self):
        """Tests if a rectangle instance is instance of Base"""
        self.assertIsInstance(Rectangle(2, 5), Base)

    def test_twoArguments(self):
        """Tests for only two arguments"""
        r = Rectangle("one", -4)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, -4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_negativeWidth(self):
        with self.assertRaises(ValueError):
            print(Rectangle(-5, 10, 1, 2, 3).width)
