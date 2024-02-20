#!/usr/bin/python3
"""Import sys and MySQLdb."""
import MySQLdb
import sys

"""Script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument"""
if __name__ == "__main__":
    """Connect to the MySQL database and list all states."""
    username, password, database_name, state_name_searched = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()

    """Use format to create the SQL query with the user input"""
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' "
                   "ORDER BY id ASC".format(state_name_searched))
    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
