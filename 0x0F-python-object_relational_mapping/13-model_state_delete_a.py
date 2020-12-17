#!/usr/bin/python3
"""
   script that prints the first State object from the database hbtn_0e_6_usa
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

    delete_row = session.query(State).filter(
        State.name.ilike('%a%')).all()

    for delete_record in delete_row:
        session.delete(delete_record)
    session.commit()
    session.close()
