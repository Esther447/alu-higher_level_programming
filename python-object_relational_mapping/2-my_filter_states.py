#!/usr/bin/python3
"""Displays all values inthe states where name matche arg from the hbtn_0e_0_usa"""
if __name__ ="__main__":
"""Access to the database and get the states from the database"""

    import MYSQLdb
    import sys
 
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    arg = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=user, port=3306,
                         passwd=password, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                WHERE name LIKE BINARY '{}'".format(arg))
    rows = cursor.fetchall()

    for i in rows:
        print(i)
    cursor.close()
    db.close()
