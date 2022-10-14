class PriceTree:
    def __init__(self):
        self.__left = None
        self.__right = None
        self.__product_code = None
        self.__price = None

    def add(self, product_code: int, price: int):
        if not isinstance(product_code, int):
            raise TypeError('Product code should be int')
        if not isinstance(price, int):
            raise TypeError('Price should be int')
        if price < 0:
            raise ValueError('Price can\'t be negative')
        if self.__product_code is None:
            self.__product_code = product_code
            self.__price = price
            return
        if product_code == self.__product_code:
            self.__price = price
        if product_code > self.__product_code:
            if self.__right is None:
                self.__right = PriceTree()
            self.__right.add(product_code, price)
            return
        if product_code < self.__product_code:
            if self.__left is None:
                self.__left = PriceTree()
            self.__left.add(product_code, price)

    def get(self, product_code: int):
        if not isinstance(product_code, int):
            raise TypeError('Product code should be int')
        if product_code == self.__product_code:
            return self.__price
        if product_code < self.__product_code:
            if self.__left is None:
                self.__no_such_product()
            return self.__left.get(product_code)
        if product_code > self.__product_code:
            if self.__right is None:
                self.__no_such_product()
            return self.__right.get(product_code)
        self.__no_such_product()

    def __no_such_product(self):
        raise ValueError('No such product')

