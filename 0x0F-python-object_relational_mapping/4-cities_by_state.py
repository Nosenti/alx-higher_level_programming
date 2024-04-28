#!/usr/bin/python3
"""
script that list all states from the db
"""
import MySQLdb
import sys


def list_cities(username, password, db_name):
    """
    Connects to MySQL db and prints states sorted
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities JOIN
    states ON state_id=states.id ORDER BY cities.id ASC"""
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_cities(username, password, dbname)
