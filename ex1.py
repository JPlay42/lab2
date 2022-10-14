class Rectangle:

    def __init__(self, width: float | int = 1, length: float | int = 1):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2*(self.length + self.width)

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @width.setter
    def width(self, width: float | int):
        if not isinstance(width, (float, int)):
            raise TypeError('Width should be float')
        if width < 0 or width > 20:
            raise ValueError('Width should be from 0 to 20')
        self.__width = width

    @length.setter
    def length(self, length: float):
        if not isinstance(length, (float, int)):
            raise TypeError('Length should be float')
        if length < 0 or length > 20:
            raise ValueError('Length should be from 0 to 20')
        self.__length = length

    def __str__(self):
        return f'Rectangle: {self.width}*{self.length}'
