#!/usr/bin/python3
""" """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ """
    def __init__(self, size, x=0, y=0, id=None):
        """ """
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        """ """
        return  self.width

    @size.setter
    def size(self, value):
        """ """
        self.width = value
        self.height = value

    def __str__(self):
        """ """
        return "[Square] ({0.id}) {0.x}/{0.y} - {0.width}".format(self)

    def update(self, *args, **kwargs):
        try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        except:
                pass
        for key, value in kwargs.items():
                try:
                    setattr(self, key, value)
                except:
                    pass

    def to_dictionary(self):
        """ """
        dic = dict(zip(["id", "size", "x", "y"], [
            self.id, self.size, self.x, self.y]))
        return dic
