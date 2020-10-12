#!/usr/bin/python3
"""  A new class was created. """


class Base():
    """ Represent class Base
        attribute:
                  __nb_objects: private attribute count the number
                                of intances created."""
    __nb_objects = 0
    def __init__(self, id=None):
        """ Initialize new intances
            args:
                 id: Int number."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
