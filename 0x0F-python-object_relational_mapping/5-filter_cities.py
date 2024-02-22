#!/usr/bin/python3
"""Import sys and MySQLdb."""
import MySQLdb
import sys

"""script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    """Connect to the MySQL database and list all states."""
    username, password, database_name, state_name_searched = sys.argv[1:4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()

    query = """SELECT cities.name FROM cities
               INNER JOIN states ON states.id=cities.state_id
               WHERE states.name=%s"""
    cursor.execute(query, (state_name_searched,))
    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]

    print(*city_names, sep=", ")

    db.close()
