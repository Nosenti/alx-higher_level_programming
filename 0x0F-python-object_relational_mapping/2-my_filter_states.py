#!/usr/bin/python3
"""
script that list all states from the db
"""
import MySQLdb
import sys


def list_states(username, password, db_name, state_name):
    """
    Connects to MySQL db and prints states sorted
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        statename = sys.argv[4]
        list_states(username, password, dbname, statename)
