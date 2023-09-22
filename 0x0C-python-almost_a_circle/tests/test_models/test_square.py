"""Test module for class Rectangle"""


from models.base import Base
from models.square import Square
import unittest


class TestRectangle(unittest.TestCase):
    """This is a test class for class Rectangle"""

    def test_positives(self):
        """test for all positive integers"""

        r = Square(5, 10, 1, 2)
        self.assertEqual(r.size, 5)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 2)

    def test_area(self):
        """test for all positive integers"""

        r = Square(5, 10, 1, 2)
        self.assertEqual(r.area(), 25)
        r = Square(5, 10, 1, 2)
        r.size = 10
        self.assertEqual(100, r.area())
        with self.assertRaises(TypeError):
            r.area(1)

    def test_negatives(self):
        """test for all negative integers"""

        with self.assertRaises(ValueError):
            r = Square(-5, 10, 1, 2)
        with self.assertRaises(ValueError):
            r = Square(5, -10, 1, 2)
        with self.assertRaises(ValueError):
            r = Square(5, 10, -1, 2)

    def test_instance(self):
        """Tests if a rectangle instance is instance of Base"""
        self.assertIsInstance(Square(2, 5), Base)

    def test_stringArgs(self):
        """Tests for only two arguments"""

        with self.assertRaises(TypeError):
            r = Square("one", 4)
        with self.assertRaises(TypeError):
            r = Square(5, "4")
        with self.assertRaises(TypeError):
            r = Square(5, 10, "1", 2)

    def test_negativeWidth(self):
        with self.assertRaises(ValueError):
            print(Square(-5, 10, 1, 3).size)
