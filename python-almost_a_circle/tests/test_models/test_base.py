#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def setUp(self):
        """Set up for testing"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test assigning an ID"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(100)
        self.assertEqual(b2.id, 100)

        b3 = Base()
        self.assertEqual(b3.id, 2)


if __name__ == "__main__":
    unittest.main()
