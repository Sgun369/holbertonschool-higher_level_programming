#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connect to the MySQL dtabase using provided credentials."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    """Create a cursor object to interact with the database."""
    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name FROM states
    INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC"""

    """Execute query"""
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
