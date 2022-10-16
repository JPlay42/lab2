class PriceTreeNode:
    def __init__(self):
        self.__left = None
        self.__right = None
        self.__product_code = None
        self.__price = None

    def add(self, product_code: int, price: int):
        if self.__product_code is None:
            self.__product_code = product_code
            self.__price = price
            return
        if product_code == self.__product_code:
            self.__price = price
        if product_code > self.__product_code:
            if not self.__right:
                self.__right = PriceTreeNode()
            self.__right.add(product_code, price)
            return
        if product_code < self.__product_code:
            if not self.__left:
                self.__left = PriceTreeNode()
            self.__left.add(product_code, price)

    def get(self, product_code: int):
        if product_code == self.__product_code:
            return self.__price
        if product_code < self.__product_code:
            if not self.__left:
                self.__no_such_product()
            return self.__left.get(product_code)
        if product_code > self.__product_code:
            if not self.__right:
                self.__no_such_product()
            return self.__right.get(product_code)
        self.__no_such_product()

    def __no_such_product(self):
        raise ValueError('No such product')


class PriceTree:

    def __init__(self):
        self.__root = PriceTreeNode()

    def add(self, product_code: int, price: int):
        if not isinstance(product_code, int):
            raise TypeError('Product code should be int')
        if not isinstance(price, int):
            raise TypeError('Price should be int')
        if price < 0:
            raise ValueError('Price can\'t be negative')
        return self.__root.add(product_code, price)

    def get(self, product_code: int):
        if not isinstance(product_code, int):
            raise TypeError('Product code should be int')
        return self.__root.get(product_code)


if __name__ == '__main__':
    tree = PriceTree()
    n_products = int(input('Amount of products: '))
    for i in range(n_products):
        code = int(input('Code: '))
        price = int(input('Price: '))
        tree.add(code, price)

    n_cart_products = int(input('Amount of products in cart: '))
    total = 0
    for i in range(n_cart_products):
        code = int(input('Code: '))
        amount = int(input('Amount: '))
        price = tree.get(code) * amount
        total += price

    print(f'Total: {total}')

