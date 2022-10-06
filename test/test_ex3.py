import unittest

from ex3 import Customer, Product, Order


class TestEx3(unittest.TestCase):
    def test_total(self):
        customer = Customer('Kuruch',
                            'Ivan',
                            'Dmytrovych',
                            '+380689724960',
                            'kuruch2004@gmail.com')

        apples = Product('Apples', 20, 'A kilo of apples.', 30, 20, 15)
        pears = Product('Pears', 25, 'A kilo of pears.')
        sardines = Product('Sardines', 40, 'A sardines can.')

        order = Order(customer)
        order.add(apples, 2)
        order.add(pears, 1)
        order.add(pears, 3)
        order.add(sardines, 5)

        # 2*20 + 4*25 + 5*40 = 340
        self.assertEqual(340, order.total())


if __name__ == '__main__':
    unittest.main()
