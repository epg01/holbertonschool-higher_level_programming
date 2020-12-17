#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


if __name__ == "__main__":
    # Nos conectamos a la base de datos.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # llamamos al metodo MetaData.create_all(), pasando nuestro "engine"
    # como fuente de conectividad de base de datos.

    Base.metadata.create_all(engine)

    # Servirá como fabrica para nuevos objetos session.

    Session = sessionmaker()

    # bind=engine una vez que el motor
    # este disponible.

    Session.configure(bind=engine)

    # siempre que necesite tener una conversación con la base de datos,
    # cree una instancia de Session

    session = Session()

    # lists all State objects from the database hbtn_0e_6_usa

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
