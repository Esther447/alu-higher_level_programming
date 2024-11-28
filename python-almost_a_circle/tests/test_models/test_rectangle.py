#!/usr/bin/python3
"""Unittest foro Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""

    def setUp(self):
        """Set up for testing"""
        self.r1 = Rectangle(10, 2)

    def test_attributes(self):
        """Test Rectangle attributes"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

    def test_area(self):
        """Test area calculation"""
        self.assertEqual(self.r1.area(), 20)


if __name__ == "__main__":
    unittest.main()
