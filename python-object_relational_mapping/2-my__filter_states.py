#!/usr/bin/ppython3
"""Displays all values in the states table of hbtn_0e_0_usa"""


import MySQLdb
import sys


if __name__ ="__main__":
    # Get MYSQL credentials, databse name, and state name from command-line arg
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MYSQL server
    db = MYSQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,,
        passsword=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    curssor = db.cursor()


    # Use format to include the state name in the query
    query = "SELECT  * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cursor.excute(query)

    # Print each row in the desired format
    for state in states:
         print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
