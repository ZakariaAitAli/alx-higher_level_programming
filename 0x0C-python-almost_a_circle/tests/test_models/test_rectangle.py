#!/usr/bin/python3
""" test cases for the Rectangle class """

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

	def test_id_generation(self):

		r1 = Rectangle(10, 2, id=1)
		r2 = Rectangle(2, 10, id=2)
		r3 = Rectangle(10, 2, 0, 0, 12)
		self.assertEqual(r1.id, 1)
		self.assertEqual(r2.id, 2)
		self.assertEqual(r3.id, 12)

	def test_height_string(self):
		with self.assertRaises(TypeError) as cm:
			Rectangle(10, "2")
		self.assertEqual(str(cm.exception), "height must be an integer")

	def test_width_negative_value(self):
		with self.assertRaises(ValueError) as cm:
			r = Rectangle(10, 2)
			r.width = -10
		self.assertEqual(str(cm.exception), "width must be > 0")

	def test_x_invalid_value(self):
		with self.assertRaises(TypeError) as cm:
			r = Rectangle(10, 2)
			r.x = {}
		self.assertEqual(str(cm.exception), "x must be an integer")

	def test_y_negative_value(self):
		with self.assertRaises(ValueError) as cm:
			Rectangle(10, 2, 3, -1)
		self.assertEqual(str(cm.exception), "y must be >= 0")

if __name__ == '__main__':
	unittest.main()
