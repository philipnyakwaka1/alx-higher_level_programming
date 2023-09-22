"""Test module for class Rectangle"""


from models.base import Base
from models.rectangle import Rectangle
import unittest
import sys
import io


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
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 4)
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 5)
        r2 = Rectangle(5, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 6)

    def test_area(self):
        """test for all positive integers"""

        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(r.area(), 50)
        r = Rectangle(5, 10, 1, 2, 3)
        r.width = 2
        r.height = 4
        self.assertEqual(8, r.area())
        with self.assertRaises(TypeError):
            r.area(1)

    def test_negatives(self):
        """test for all negative integers"""

        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10, 1, 2, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10, 1, 2, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -1, 2, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 1, -2, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 7)

    def test_instance(self):
        """Tests if a rectangle instance is instance of Base"""
        self.assertIsInstance(Rectangle(2, 5), Base)

    def test_stringArgs(self):
        """Tests for only two arguments"""

        with self.assertRaises(TypeError):
            r = Rectangle("one", 4)
        with self.assertRaises(TypeError):
            r = Rectangle(5, "4")
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 1, "2", 3)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "1", 2, 3)

    def test_negativeWidth(self):
        with self.assertRaises(ValueError):
            print(Rectangle(-5, 10, 1, 2, 3).width)

    def test_print(self):
        r = Rectangle(10, 15)
        self.assertEqual(r.__str__(), "[Rectangle] (7) 0/0 - 10/15")

    def test_display1(self):
        r = Rectangle(3, 5)
        with self.assertRaises(TypeError):
            r.display(1)
