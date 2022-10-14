import unittest

from ex1 import Rectangle


class TestEx1(unittest.TestCase):
    def test_perimeter(self):
        rectangle = Rectangle(3, 5)
        self.assertEqual(16, rectangle.perimeter())

    def test_input_types(self):
        rectangle = Rectangle(0, 0)
        with self.assertRaises(TypeError):
            rectangle.width = 'hello'
        with self.assertRaises(TypeError):
            rectangle.length = 'world'
        with self.assertRaises(TypeError):
            Rectangle('lorem', 0)
        with self.assertRaises(TypeError):
            Rectangle(0, 'ipsum')

    def test_width_limits(self):
        rectangle = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            rectangle.width = -1
        with self.assertRaises(ValueError):
            rectangle.width = 21

    def test_length_limits(self):
        rectangle = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            rectangle.length = -1
        with self.assertRaises(ValueError):
            rectangle.length = 21

    def test_default_values(self):
        rectangle = Rectangle()
        self.assertEqual(1, rectangle.width)
        self.assertEqual(1, rectangle.length)

    def test_str(self):
        rectangle = Rectangle(3, 5)
        self.assertEqual('Rectangle: 3*5', str(rectangle))


if __name__ == '__main__':
    unittest.main()
