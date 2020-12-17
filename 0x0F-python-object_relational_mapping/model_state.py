#!/usr/bin/python3
"""
   Python file that contains the class definition of a
   State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Args:
        Base ([type]): [description]
    """
    # Enlaces a los estados de la tabla States.

    __tablename__ = 'states'

    # id de atributo de clase que representa una columna de un entero
    # único generado automáticamente, no puede ser nulo y es una clave principa

    id = Column(Integer, primary_key=True)

    # Atributo de clase (name) que representa una columna de una
    # cadena con un máximo de 128 caracteres y no puede ser nulo

    name = Column(String(128), nullable=False)
