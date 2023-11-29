#!/usr/bin/python3
"""a script that prints the first State object
from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """connect to the database"""
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    """create the SQLAlchemy engine"""
    engine = create_engine(connection, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    """create a session to interact with the database"""

    with Session(engine) as session:
        first_state = session.query(State).first()
        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")
