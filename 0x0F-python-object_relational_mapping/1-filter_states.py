#!/usr/bin/python3
"""import sys and mysqldb"""
import MySQLdb
import sys

"""script that lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    """Connect to the MySQL database and list all states
    """
    username, password, database_name = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'"
                   "ORDER BY states.id ASC")
    states = cursor.fetchall()

    seen_states = set()
    filtered_states = []
    for state in states:
        if state[1] not in seen_states:
            filtered_states.append(state)
            seen_states.add(state[1])

    for state in states:
        print(state)

    db.close()
