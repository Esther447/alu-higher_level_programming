#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the
states table of a database where the name matches the given argument.
It uses the MySQLdb module and prevents SQL injection.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if sufficient arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./script.py <mysql_user> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    try:
        # Connect to the MySQL database
        conn = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host="localhost",
            port=3306
        )
        cursor = conn.cursor()

        # Use a parameterized query to prevent SQL injection
        query = """
        SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC
        """
        cursor.execute(query, (sys.argv[4],))

        # Fetch and display results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        # Ensure resources are closed
        cursor.close()
        conn.close()
