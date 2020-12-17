#!/usr/bin/python3
"""
   Python file that contains the class definition of a City.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class City(model_state):
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

    # Atributo de clase state_id que representa una columna de un número
    # entero, no puede ser nulo y es una clave externa para estados.id

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
