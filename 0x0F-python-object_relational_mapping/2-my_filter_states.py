#!/usr/bin/python3
"""Python_ SQL code"""

import sys
import MySQLdb

def search_states(username, password, database, state_name):
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(
                host='localhost',
                user=username,
                passwd=password,
                db=database,
                port=3306
                )
        cursor = connection.cursor()

        # Execute query to retrieve states matching the state_name
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' "
                       "ORDER BY id ASC".format(state_name))

        states = cursor.fetchall()

        # Display states
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close connection
        if connection:
            connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> "
              "<password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, database, state_name)
