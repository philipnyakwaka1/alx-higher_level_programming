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
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id - r1.id, 1)
        r3 = Rectangle(5, 2)
        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id - r2.id, 1)

    def test_area(self):
        """test for all positive integers"""

        r4 = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(r4.area(), 50)
        r5 = Rectangle(5, 10, 1, 2, 3)
        r5.width = 2
        r5.height = 4
        self.assertEqual(8, r5.area())
        with self.assertRaises(TypeError):
            r5.area(1)

    def test_negatives(self):
        """test for all negative integers"""

        with self.assertRaises(ValueError):
            r6 = Rectangle(-5, 10, 1, 2, 3)
        with self.assertRaises(ValueError):
            r7 = Rectangle(5, -10, 1, 2, 3)
        with self.assertRaises(ValueError):
            r8 = Rectangle(5, 10, -1, 2, 3)
        with self.assertRaises(ValueError):
            r9 = Rectangle(5, 10, 1, -2, 3)
        with self.assertRaises(ValueError):
            r10 = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            r11 = Rectangle(0, 7)

    def test_instance(self):
        """Tests if a rectangle instance is instance of Base"""
        r12 = Rectangle(2, 5)
        self.assertIsInstance(r12, Base)

    def test_stringArgs(self):
        """Tests for only two arguments"""

        with self.assertRaises(TypeError):
            r13 = Rectangle("one", 4)
        with self.assertRaises(TypeError):
            r14 = Rectangle(5, "4")
        with self.assertRaises(TypeError):
            r15 = Rectangle(5, 10, 1, "2", 3)
        with self.assertRaises(TypeError):
            r16 = Rectangle(5, 10, "1", 2, 3)

    def test_negativeWidth(self):
        with self.assertRaises(ValueError):
            print(Rectangle(-5, 10, 1, 2, 3).width)

    def test_print(self):
        r17 = Rectangle(10, 15)
        self.assertEqual(type(r17.__str__()), str)

    def test_toDictionary(self):
        self.assertEqual(Rectangle(2, 4, 0, 0, 5).to_dictionary(), {
                         'id': 5, 'width': 2, 'height': 4, 'x': 0, 'y': 0})

    def test_update(self):
        r = Rectangle(2, 4, 0, 0, 5)
        r.update()
        self.assertEqual(r.to_dictionary(), {
                         'id': 5, 'width': 2, 'height': 4, 'x': 0, 'y': 0})
        r = Rectangle(2, 4, 0, 0, 5)
        r.update(90)
        self.assertEqual(r.to_dictionary(), {
                         'id': 90, 'width': 2, 'height': 4, 'x': 0, 'y': 0})
        r = Rectangle(2, 4, 0, 0, 5)
        r.update(90, 2)
        self.assertEqual(r.to_dictionary(), {
                         'id': 90, 'width': 2, 'height': 4, 'x': 0, 'y': 0})
        r = Rectangle(2, 4, 0, 0, 5)
        r.update(90, 2, 5)
        self.assertEqual(r.to_dictionary(), {
                         'id': 90, 'width': 2, 'height': 5, 'x': 0, 'y': 0})
        r = Rectangle(2, 4, 0, 0, 5)
        r.update(90, 2, 5, 6)
        self.assertEqual(r.to_dictionary(),
                         {'id': 90, 'width': 2, 'height': 5, 'x': 6, 'y': 0})
        r = Rectangle(2, 4, 0, 0, 5)
        r.update(90, 2, 5, 6, 8)
        self.assertEqual(r.to_dictionary(),
                         {'id': 90, 'width': 2, 'height': 5, 'x': 6, 'y': 8})
        r = Rectangle(2, 4, 0, 0, 5)
        r.update(**{'id': 89})
        self.assertEqual(r.to_dictionary(),
                         {'id': 89, 'width': 2, 'height': 4, 'x': 0, 'y': 0})

    def test_create(self):
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.to_dictionary(),
                         {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_saveToFile(self):
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])
