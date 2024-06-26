#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_states(mysql_username, mysql_password, database_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON states.id = cities.state_id
        ORDER BY cities.id ASC
        """
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(mysql_username, mysql_password, database_name)
