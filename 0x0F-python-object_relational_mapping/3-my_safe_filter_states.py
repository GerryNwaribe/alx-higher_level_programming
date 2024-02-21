#!/usr/bin/python3
"""Import sys and MySQLdb."""
import MySQLdb
import sys

"""Script that safe from MySQL injections"""
if __name__ == "__main__":
    """Connect to the MySQL database and list all states."""
    username, password, database_name, state_name_searched = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()

    """Use format to create the SQL query with the user input"""
    query = "SELECT * FROM states WHERE name LIKE %s"
    cursor.execute(query, (state_name_searched))
    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
