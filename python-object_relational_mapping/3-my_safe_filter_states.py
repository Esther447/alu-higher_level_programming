#!/usr/bin/python3
"""
This script takes in four arguments:
1. MySQL username
2. MySQL password
3. Database name
4. State name to search

It displays all values in the `states` table where `name`
matches the argument, protecting against SQL injection.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Safe query using parameterized statements
    query = """
    SELECT * FROM states
    WHERE name = %s
    ORDER BY id ASC;
    """
    cursor.execute(query, (state_name,))

    # Fetch all matching rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
