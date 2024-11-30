#!/usr/bin/python3
"""
Lists all cities from the database `hbtn_0e_4_usa`.

The script takes 3 arguments:
1. MySQL username
2. MySQL password
3. Database name

It connects to a MySQL server running on localhost at port 3306 and
displays results sorted in ascending order by `cities.id`.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Query to fetch cities with corresponding state names
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    # Fetch all results
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
