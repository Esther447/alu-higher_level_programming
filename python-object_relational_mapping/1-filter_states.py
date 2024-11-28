#!/usr/bin/python3
"""Script that lists all states with a name starting with N(upper N)"""


import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to fetch states starting with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    # Fetch all rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
