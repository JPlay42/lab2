import io
import unittest
from unittest.mock import patch

from ex6 import PriceTree, count_total


class TestEx6(unittest.TestCase):
    def test_validation(self):
        tree = PriceTree()
        with self.assertRaises(TypeError):
            tree.add('not a code', 1234)
        with self.assertRaises(TypeError):
            tree.add(1234, 'not a price')
        with self.assertRaises(ValueError):
            tree.add(1234, -5)
        with self.assertRaises(TypeError):
            tree.get('not an int')

    def test_tree(self):
        tree = PriceTree()
        tree.add(5, 50)
        tree.add(6, 35)
        tree.add(3, 80)
        tree.add(9, 65)
        tree.add(7, 123)
        tree.add(1, 2)

        self.assertEqual(50, tree.get(5))
        self.assertEqual(35, tree.get(6))
        self.assertEqual(80, tree.get(3))
        self.assertEqual(65, tree.get(9))
        self.assertEqual(123, tree.get(7))
        self.assertEqual(2, tree.get(1))
        with self.assertRaises(ValueError):
            tree.get(18)


if __name__ == '__main__':
    unittest.main()
