#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to the MySQL dtabae using provided credentials.
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    # Create a cursor object to interact with the database.
    cur = db.cursor()

    # Execute a SQL query to select all stated from the 'stats' table.
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the SQL query.
    rows = cur.fetchall()
    # print each row representing a state in the database.
for row in rows:
    print(row)
