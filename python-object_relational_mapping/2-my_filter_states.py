#!/usr/bin/python3
"""a script that takes in an argument and displays
all values in the states table
of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connect to the MySQL dtabae using provided credentials."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )

    """Create a cursor object to interact with the database."""
    cursor = db.cursor()

    query = """SELECT *
    FROM states
    WHERE name = '{}' ORDER BY id ASC """.format(argv[4])

    state_name = argv[4]
    """query to execute"""

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
