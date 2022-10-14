from math import gcd


class Rational:

    def __init__(self, numerator: int = 1, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, numerator: int):
        if not isinstance(numerator, int):
            raise TypeError('Numerator should be int')
        self.__numerator = numerator

    @denominator.setter
    def denominator(self, denominator: int):
        if not isinstance(denominator, int):
            raise TypeError('Denominator should be int')
        if denominator == 0:
            raise ValueError('Divide by zero')
        self.__denominator = denominator

    def float(self):
        return self.__numerator / self.__denominator

    def __str__(self):
        common_divider = gcd(self.numerator, self.denominator)
        return f'{self.numerator//common_divider}/' \
               f'{self.denominator//common_divider}'
