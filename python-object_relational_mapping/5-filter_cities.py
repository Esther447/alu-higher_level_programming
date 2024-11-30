#!/usr/bin/python3
"""
Lists all cities of a state in the database 'hbtn_0e_4_usa'
 safe from SQL injection.
"""

import MYSQLbd
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]


    db = MYSQLdb.connect(
        host="localhost",
        port=mysql_password,
        password=mysql_password,
        db=db_name
     )



     cur = db.cursor()
    

     querry = """
          SELECT cotoes.name
          FROM cities
          JOIN states ON cities.state_id = states.id
          WHERE states.name = %s
          ORDER BY cities.id ASC
     """
     cur execute(query, (state_name,))


     cities = cur.fetchall()


     print(", ".join(city[0] for city in cities))


     cur.close()
     db.close()
