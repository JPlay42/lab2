class Rectangle:
    __width: float
    __length: float

    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2*(self.__length + self.__width)

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @width.setter
    def width(self, width: float):
        if not isinstance(width, float):
            raise TypeError('Width should be float')
        if width < 0 or width > 20:
            raise ValueError('Width should be from 0 to 20')
        self.__width = width

    @length.setter
    def length(self, length: float):
        if not isinstance(length, float):
            raise TypeError('Length should be float')
        if length < 0 or length > 20:
            raise ValueError('Length should be from 0 to 20')
        self.__length = length
