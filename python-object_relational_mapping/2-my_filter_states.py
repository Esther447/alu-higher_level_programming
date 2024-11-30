#!/usr/bin/python3
"""Display all values in the states"""


import sys
import MYSQLdb


if __name__ == "__main__":
    conn = MYSQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=33306
    )
    cursor = conn.cursor()
    sql = """SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY id ASC """.format(sys.argv[4])
