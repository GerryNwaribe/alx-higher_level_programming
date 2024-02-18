#!/usr/bin/python3
import MySQLdb
import sys

"""script that lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    username, password, database_name = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
