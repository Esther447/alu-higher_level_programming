#!/usr/bin/python3
"""
Lists all State objects containing the letter 'a' from the specified database.

Usage:
    ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>
"""

from model_state import Base, State  # Import SQLAlchemy ORM models
from sqlalchemy import create_engine  # For connecting to the MySQL database
from sqlalchemy.orm import sessionmaker  # For creating a session to interact with the database
import sys  # To handle command-line arguments

def main():
    """Main function to connect to the database and query states containing 'a'."""
    # Retrieve arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine and session to interact with the database
    engine = create_engine(f'mysql+mysqlconnector://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states with 'a' in their name, sorted by state.id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print results in the required format
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
