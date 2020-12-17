#!/usr/bin/python3
"""
   Script that prints the State object with the name passed as
   argument from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


if __name__ == '__main__':
    # Nos conectamos a la base de datos.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # llamamos al metodo MetaData.create_all(), pasando nuestro "engine"
    # como fuente de conectividad de base de datos.

    Base.metadata.create_all(engine)

    Session = sessionmaker()

    # bind=engine una vez que el motor
    # este disponible.

    Session.configure(bind=engine)

    # siempre que necesite tener una conversación con la base de datos,
    # cree una instancia de Session

    session = Session()

    Find_ob = session.query(State).order_by(State.id).filter(
        State.name == sys.argv[4]).all()

    if len(Find_ob):
        for id_ob in Find_ob:
            print("{}".format(id_ob.id))
    else:
        print("Not found")

    session.close()
