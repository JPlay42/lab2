import unittest

from ex3 import Customer, Product, Order


class TestEx3(unittest.TestCase):
    def test_customer_validation(self):
        # all fields are non-empty strings
        Customer('a', 'b', 'c', 'd', 'e')
        with self.assertRaises(TypeError):
            Customer(1, 'b', 'c', 'd', 'e')
        with self.assertRaises(TypeError):
            Customer('a', 2, 'c', 'd', 'e')
        with self.assertRaises(TypeError):
            Customer('a', 'b', 3, 'd', 'e')
        with self.assertRaises(TypeError):
            Customer('a', 'b', 'c', 4, 'e')
        with self.assertRaises(TypeError):
            Customer('a', 'b', 'c', 'd', 5)
        with self.assertRaises(ValueError):
            Customer('', 'b', 'c', 'd', 'e')
        with self.assertRaises(ValueError):
            Customer('a', '', 'c', 'd', 'e')
        with self.assertRaises(ValueError):
            Customer('a', 'b', '', 'd', 'e')
        with self.assertRaises(ValueError):
            Customer('a', 'b', 'c', '', 'e')
        with self.assertRaises(ValueError):
            Customer('a', 'b', 'c', 'd', '')

    def test_customer_str(self):
        customer = Customer('Kuruch',
                            'Ivan',
                            'Dmytrovych',
                            '+380689724960',
                            'kuruch2004@gmail.com')
        self.assertEqual('Customer: Kuruch Ivan Dmytrovych, '
                         'phone: +380689724960, '
                         'email: kuruch2004@gmail.com', str(customer))

    def test_product_validation(self):
        Product('1', 2, '3')
        Product('1', 2, '3', 4, 5, 6)
        with self.assertRaises(TypeError):
            Product(1, 2, '3')  # int instead of name
        with self.assertRaises(TypeError):
            Product('1', '2', '3')  # str instead of price
        with self.assertRaises(TypeError):
            Product('1', 2, 3)  # int instead of description
        with self.assertRaises(TypeError):
            Product('1', 2, '3', '4')  # str instead of x
        with self.assertRaises(TypeError):
            Product('1', 2, '3', 4, '5')  # str instead of y
        with self.assertRaises(TypeError):
            Product('1', 2, '3', 4, 5, '6')  # str instead of z
        with self.assertRaises(ValueError):
            Product('', 2, '3')  # empty name
        with self.assertRaises(ValueError):
            Product('1', -1, '3')  # price is negative
        with self.assertRaises(ValueError):
            Product('1', 2, '3', -1)  # x is negative
        with self.assertRaises(ValueError):
            Product('1', 2, '3', 4, -1)  # y is negative
        with self.assertRaises(ValueError):
            Product('1', 2, '3', 4, 5, -1)  # z is negative

    def test_product_str(self):
        apples = Product('Apples', 20, 'A kilo of apples.', 30, 20, 15)
        self.assertEqual('Product: \"Apples\", A kilo of apples., '
                         '20 UAH, 30*20*15 cm', str(apples))

    def test_order_validation(self):
        with self.assertRaises(TypeError):
            Order('definitely_not_customer')
        customer = Customer('A', 'B', 'C', '+12345', 'a@b.c')
        order = Order(customer)
        product = Product('Harry Potter', 228)
        with self.assertRaises(TypeError):
            order.add('definitely_not_product', 3)
        with self.assertRaises(TypeError):
            order.add(product, 'not an integer')
        with self.assertRaises(ValueError):
            order.add(product, 0)
        order.add(product, 1)

    def test_order(self):
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

        # test order __str__
        self.assertEqual('Order: 2x Apples; 4x Pears; 5x Sardines; ', str(order))

        # 2*20 + 4*25 + 5*40 = 340
        self.assertEqual(340, order.total())


if __name__ == '__main__':
    unittest.main()
