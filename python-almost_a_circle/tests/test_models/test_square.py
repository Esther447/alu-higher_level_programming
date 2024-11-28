#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square



class TestSquare(unittest.TestCase):
    """Tests for the Square class"""

    def setUp(self):
        """Set up for testing"""
        self.s1 = Square(5)

    def test_size(self):
        """Test Square size attribute"""
        self.assertEqual(self.s1.size, 5)

    def test_area(self):
        """Test area calculation"""
        self.assertEqual(self.s1.area(), 25)


if __name__ == "__main__":
    unittest.main()
