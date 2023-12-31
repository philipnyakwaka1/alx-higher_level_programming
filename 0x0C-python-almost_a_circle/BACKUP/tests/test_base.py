"""Test for the Base class"""

import unittest
import sys
from models.base import Base


class TestBase(unittest.TestCase):
    """This is a test class for the Base class"""

    def test_id(self):
        """This functions tests the getter method for id"""
        test_object = Base()
        self.assertEqual(test_object.id, 1)

    def test_setId(self):
        """This function tests the id setter method"""

        test_object = Base(1)
        test_object.id = 3
        self.assertEqual(test_object.id, 3)

    def test_negative(self):
        """Test for negative id"""

        test_object = Base(-1)
        self.assertEqual(test_object.id, -1)

    def test_zero(self):
        """Test for zero id"""

        test_object = Base(0)
        self.assertEqual(test_object.id, 0)

    def test_baseToString(self):
        self.assertEqual(type(Base.to_json_string([{'id': 12}])), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 5}]), '[{"id": 5}]')

    def test_fromJson(self):
        self.assertEqual(Base.from_json_string('[{ "id": 5 }]'), [{"id": 5}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])
