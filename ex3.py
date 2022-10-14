class Product:

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

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price_uah(self):
        return self.__price_uah

    @property
    def x_cm(self):
        return self.__x_cm

    @property
    def y_cm(self):
        return self.__y_cm

    @property
    def z_cm(self):
        return self.__z_cm

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Name should be str')
        if name == '':
            raise ValueError('Name should not be empty')
        self.__name = name

    @description.setter
    def description(self, description: str):
        if not isinstance(description, str):
            raise TypeError('Description should be str')
        self.__description = description

    @price_uah.setter
    def price_uah(self, price_uah: int):
        if not isinstance(price_uah, int):
            raise TypeError('Price should be int')
        if price_uah < 0:
            raise ValueError('Price can\'t be negative')
        self.__price_uah = price_uah

    @x_cm.setter
    def x_cm(self, x_cm: int):
        if not isinstance(x_cm, int):
            raise TypeError('X should be int')
        if x_cm < 0:
            raise ValueError('X cannot be negative')
        self.__x_cm = x_cm

    @y_cm.setter
    def y_cm(self, y_cm: int):
        if not isinstance(y_cm, int):
            raise TypeError('Y should be int')
        if y_cm < 0:
            raise ValueError('Y cannot be negative')
        self.__y_cm = y_cm

    @z_cm.setter
    def z_cm(self, z_cm: int):
        if not isinstance(z_cm, int):
            raise TypeError('Z should be int')
        if z_cm < 0:
            raise ValueError('Z cannot be negative')
        self.__z_cm = z_cm

    def __str__(self):
        return f'Product: \"{self.name}\", ' \
                f'{self.description}, ' \
                f'{self.price_uah} UAH, ' \
                f'{self.x_cm}*{self.y_cm}*{self.z_cm} cm'


class Customer:

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

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    @surname.setter
    def surname(self, surname: str):
        if not isinstance(surname, str):
            raise TypeError('Surname should be str')
        if surname == '':
            raise ValueError('Surname can\'t be empty')
        self.__surname = surname

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Name should be str')
        if name == '':
            raise ValueError('Name can\'t be empty')
        self.__name = name

    @patronymic.setter
    def patronymic(self, patronymic: str):
        if not isinstance(patronymic, str):
            raise TypeError('Patronymic should be str')
        if patronymic == '':
            raise ValueError('Patronymic can\'t be empty')
        self.__patronymic = patronymic

    @phone.setter
    def phone(self, phone: str):
        if not isinstance(phone, str):
            raise TypeError('Phone should be str')
        if phone == '':
            raise ValueError('Phone can\'t be empty')
        self.__phone = phone

    @email.setter
    def email(self, email: str):
        if not isinstance(email, str):
            raise TypeError('Email should be str')
        if email == '':
            raise ValueError('Email can\'t be empty')
        self.__email = email

    def __str__(self):
        return f'Customer: {self.surname} {self.name} {self.patronymic}, ' \
                f'phone: {self.phone}, email: {self.email}'


class Order:
    __product_amounts: dict

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__product_amounts = dict()

    def add(self, product: Product, add_amount: int):
        if not isinstance(product, Product):
            raise TypeError('Wrong type of product')
        if not isinstance(add_amount, int):
            raise TypeError('Add_amount should be int')
        if add_amount <= 0:
            raise ValueError('Add_amount should be positive')
        amount = self.__product_amounts.get(product, 0)
        amount += add_amount
        self.__product_amounts[product] = amount

    def total(self):
        total = 0
        for product in self.__product_amounts:
            total += product.price_uah * self.__product_amounts[product]
        return total

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer: Customer):
        if not isinstance(customer, Customer):
            raise TypeError('Wrong type of customer')
        self.__customer = customer

    def __str__(self):
        result = 'Order: '
        for product in self.__product_amounts:
            result += f'{self.__product_amounts[product]}x ' \
                      f'{product.name}; '
        return result
