class Product:
    name: str
    price_uah: int
    description: str
    x_cm: int
    y_cm: int
    z_cm: int

    def __init__(self,
                 name: str,
                 price_uah: int,
                 description: str = "",
                 x_cm: int = 10,
                 y_cm: int = 10,
                 z_cm: int = 10):
        self.name = name
        self.price_uah = price_uah
        self.description = description
        self.x_cm = x_cm
        self.y_cm = y_cm
        self.z_cm = z_cm


class Customer:
    surname: str
    name: str
    patronymic: str
    phone: str
    email: str

    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 phone: str,
                 email: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone
        self.email = email


class Order:
    customer: Customer
    __product_amounts: dict

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__product_amounts = dict()

    def add(self, product: Product, add_amount: int):
        amount = self.__product_amounts.get(product, 0)
        amount += add_amount
        self.__product_amounts[product] = amount

    def total(self):
        total = 0
        for product in self.__product_amounts:
            total += product.price_uah * self.__product_amounts[product]
        return total
