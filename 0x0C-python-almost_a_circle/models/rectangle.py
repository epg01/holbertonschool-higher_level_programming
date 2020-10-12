#!/usr/bin/python3
""" """
from models.base import Base

class Rectangle(Base):
    """ """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ """
        return self.__width

    @width.setter
    def width(self, value):
        """ """
        Rectangle.Handle_error('width', value)
        self.__width = value

    @property
    def height(self):
        """ """
        return self.__height

    @height.setter
    def height(self, value):
        """ """
        Rectangle.Handle_error('height', value)
        self.__height = value

    @property
    def y(self):
        """ """
        return self.__y

    @y.setter
    def y(self, value):
        """ """
        Rectangle.Handle_error('y', value)
        self.__y = value

    @property
    def x(self):
        """ """
        return self.__x

    @x.setter
    def x(self, value):
        """ """
        Rectangle.Handle_error('x', value)
        self.__x = value

    @staticmethod
    def Handle_error(Name_Attribute, value):
        """ """
        if type(value) != int:
            raise TypeError("{0} must be an integer".format(Name_Attribute))
        if Name_Attribute in ["width", "height"] and value <= 0:
            raise ValueError("{0} must be > 0".format(Name_Attribute))
        if Name_Attribute in ["x", "y"] and value < 0:
            raise ValueError("{0} must be >= 0".format(Name_Attribute))

    def area(self):
        """ """
        return self.width * self.height

    def display(self):
        """ """
        print("{0}".format(self.y * '\n'), end='')
        for value in range(self.height):
            print("{0}".format(self.x * ' '), end='')
            print(self.width * "#")

    def __str__(self):
        return "[Rectangle] ({0.id}) {0.x}/{0.y} - {0.width}/{0.height}".format(self)

    def update(self, *args, **kwargs):
        try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        except:
                pass
        for key, value in kwargs.items():
                try:
                    setattr(self, key, value)
                except:
                    pass
    def to_dictionary(self):
        dic = {}
        for i in ["id", "width", "height", "x", "y"]:
            dic[i] = getattr(self, i)
        return dic
