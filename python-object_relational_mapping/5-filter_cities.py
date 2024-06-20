#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_states(mysql_username, mysql_password, database_name, state_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        """
    cursor.execute(query, (state_name,))

    states = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    list_states(mysql_username, mysql_password, database_name, state_name)
