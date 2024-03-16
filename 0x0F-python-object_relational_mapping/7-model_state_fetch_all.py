#!/usr/bin/python3
"""script that lists all State
objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Database connection parameters
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db_connection = ('mysql+mysqldb://{}:{}@localhost:3306/{}'
                     .format(username, password, db_name))

    # Create engine and bind it to the Base class
    engine = create_engine(db_connection)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and print them
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
