#!/usr/bin/python3
"""
script that list all states from the db
"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connects to MySQL db and prints states sorted
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
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
        list_states(username, password, dbname)
