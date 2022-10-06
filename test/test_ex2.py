import unittest

from ex2 import Rational


class TestEx2(unittest.TestCase):
    def test_number_forms(self):
        number = Rational(3, 4)
        self.assertEqual(0.75, number.float())
        self.assertEqual('3/4', str(number))

    def test_reduction(self):
        number = Rational(30, 90)
        self.assertEqual('1/3', str(number))

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Rational(1, 0)

    def test_default_values(self):
        number_without_numerator = Rational(denominator=4)
        self.assertEqual(0.25, number_without_numerator.float())
        number_without_denominator = Rational(numerator=5)
        self.assertEqual(5, number_without_denominator.float())
        number_without_anything = Rational()
        self.assertEqual(1, number_without_anything.float())


if __name__ == '__main__':
    unittest.main()
