"""Test module for class Rectangle"""


from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
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

    def test_print(self):
        r17 = Square(10, 15)
        self.assertEqual(type(r17.__str__()), str)

    def test_toDictionary(self):
        self.assertEqual(Square(2, 4, 0, 0).to_dictionary(), {
                         'id': 0, 'size': 2, 'x': 4, 'y': 0})

    def test_update(self):
        r = Square(2, 4, 0, 0)
        r.update()
        self.assertEqual(r.to_dictionary(),
                         {'id': 0, 'size': 2, 'x': 4, 'y': 0})
        r = Square(2, 4, 0, 0)
        r.update(90)
        self.assertEqual(r.to_dictionary(), {
                         'id': 90, 'size': 2, 'x': 4, 'y': 0})
        r = Square(2, 4, 0, 0)
        r.update(90, 2)
        self.assertEqual(r.to_dictionary(), {
                         'id': 90, 'size': 2, 'x': 4, 'y': 0})
        r = Square(2, 4, 0, 0)
        r.update(90, 2, 5)
        self.assertEqual(r.to_dictionary(), {
                         'id': 90, 'size': 2, 'x': 5, 'y': 0})
        r = Square(2, 4, 0, 0)
        r.update(90, 2, 5, 6)
        self.assertEqual(r.to_dictionary(),
                         {'id': 90, 'size': 2, 'x': 5, 'y': 6})
        r = Square(2, 4, 0, 0)
        r.update(**{'id': 89})
        self.assertEqual(r.to_dictionary(),
                         {'id': 89, 'size': 2, 'x': 4, 'y': 0})

    def test_create(self):
        r = Square.create(
            **{'id': 89, 'size': 1, 'x': 3, 'y': 4})
        self.assertEqual(r.to_dictionary(),
                         {'id': 89, 'size': 1, 'x': 3, 'y': 4})

    def test_saveToFile(self):
        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])
        a = Square.save_to_file([Square(1)])
        b = Square.load_from_file()
        self.assertEqual(len(b), 1)

    def test_loadEmpty(self):
        b = Square.load_from_file()
        self.assertEqual(len(b), 1)
