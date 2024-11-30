#!/usr/bin/python3
"""
Lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for all State objects containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")
