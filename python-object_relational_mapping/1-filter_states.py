#!/usr/bin/python3
"""a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connect to the MySQL dtabae using provided credentials."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    """Create a cursor object to interact with the database."""
    cursor = db.cursor()

    """Execute a SQL query to select all stated from the 'stats' table."""
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    """Fetch all the rows returned by the SQL query"""
    rows = cursor.fetchall()

    """Prints rows where the second column of the result starts with 'N'"""
    for row in rows:
        if row[1][0] == 'N':
            print(row)

