#!/usr/bin/python3
"""  a script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa"""
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

    query = """SELECT cities.name
    FROM states
    INNER JOIN cities ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC"""
    cursor.execute(query, (argv[4],))

    results = cursor.fetchall()

    city_names = [row[0] for row in results]
    print(', '.join(city_names))