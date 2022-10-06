import unittest

from ex1 import Rectangle


class TestEx1(unittest.TestCase):
    def test_perimeter(self):
        rectangle = Rectangle(3, 5)
        self.assertEqual(16, rectangle.perimeter())

    def test_set_width_limits(self):
        rectangle = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            rectangle.width = -1
        with self.assertRaises(ValueError):
            rectangle.width = 21

    def test_set_length_limits(self):
        rectangle = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            rectangle.length = -1
        with self.assertRaises(ValueError):
            rectangle.length = 21

    def test_constructor_limits(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 0)
        with self.assertRaises(ValueError):
            Rectangle(21, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, -1)
        with self.assertRaises(ValueError):
            Rectangle(0, 21)


if __name__ == '__main__':
    unittest.main()
