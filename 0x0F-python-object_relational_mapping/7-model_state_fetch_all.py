#!/usr/bin/python3
"""
script that lists all State objects
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Extract MySQL connection information from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    # Base.metadata.create_all(engine)

    # Create session maker
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query and list all State objects
    states = session.query(State).order_by(State.id).all()

    # Display the results with specific formatting
    for state in states:
        print(state.id, state.name, sep=": ")

    # Close session
    session.close()
