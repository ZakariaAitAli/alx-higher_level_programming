#!/usr/bin/python3

""" test cases for the Base class """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def test_id_generation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, b2.id + 1)

    def test_custom_id(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_incremental_id(self):
        b5 = Base()
        b6 = Base()
        self.assertEqual(b6.id, b5.id + 1)

if __name__ == '__main__':
    unittest.main()
