#!/usr/bin/python3
""" test cases for the Rectangle class """

import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):

	def setUp(self):
		Rectangle.reset_id()

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

	def test_area(self):
		r1 = Rectangle(3, 2)
		self.assertEqual(r1.area(), 6)

		r2 = Rectangle(2, 10)
		self.assertEqual(r2.area(), 20)

		r3 = Rectangle(8, 7, 0, 0, 12)
		self.assertEqual(r3.area(), 56)

	def test_display(self):
		captured_output = StringIO()
		sys.stdout = captured_output

		r1 = Rectangle(4, 6)
		r1.display()

		sys.stdout = sys.__stdout__

		printed_output = captured_output.getvalue()

		expected_output = "####\n####\n####\n####\n####\n####\n"

		self.assertEqual(printed_output, expected_output)

		captured_output = StringIO()
		sys.stdout = captured_output

		r2 = Rectangle(2, 2)
		r2.display()

		sys.stdout = sys.__stdout__
		printed_output = captured_output.getvalue()
		expected_output = "##\n##\n"
		self.assertEqual(printed_output, expected_output)

	def test_str_representation(self):
		r1 = Rectangle(4, 6, 2, 1, 12)
		self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

		r2 = Rectangle(5, 5, 1)
		self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

	def test_display(self):
		captured_output = StringIO()
		sys.stdout = captured_output

		r1 = Rectangle(2, 3, 2, 2)
		r1.display()

		sys.stdout = sys.__stdout__
		printed_output = captured_output.getvalue()
		expected_output = "\n\n  ##\n  ##\n  ##\n"
		self.assertEqual(printed_output, expected_output)

		captured_output = StringIO()
		sys.stdout = captured_output

		r2 = Rectangle(3, 2, 1, 0)
		r2.display()

		sys.stdout = sys.__stdout__
		printed_output = captured_output.getvalue()
		expected_output = " ###\n ###\n"
		self.assertEqual(printed_output, expected_output)
		
	def test_update(self):
		r = Rectangle(10, 10, 10, 10)
		self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

		r.update(89)
		self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

		r.update(89, 2)
		self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

		r.update(89, 2, 3)
		self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

		r.update(89, 2, 3, 4)
		self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")

		r.update(89, 2, 3, 4, 5)
		self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

if __name__ == '__main__':
	unittest.main()
