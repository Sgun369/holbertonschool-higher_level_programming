#!/usr/bin/python3
"""write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
 But this time, it is one that is safe from MySQL injections!"""
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

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    state_name = argv[4]

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        if row[1] == state_name:
            print(row)

    cursor.close()
    db.close()
