from math import gcd


class Rational:
    __numerator: int
    __denominator: int

    def __init__(self, numerator: int = 1, denominator: int = 1):
        if denominator == 0:
            raise ValueError('Divide by zero')
        common_divider = gcd(numerator, denominator)
        self.__numerator = numerator // common_divider
        self.__denominator = denominator // common_divider

    def float(self):
        return self.__numerator / self.__denominator

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'
