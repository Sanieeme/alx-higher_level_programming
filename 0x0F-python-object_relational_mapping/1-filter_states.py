#!/usr/bin/python3
import MySQLdb
import sys
"""script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY states.id")

    states = c.fetchall()

    for state in states:
        print(state)

    c.close()
    db.close()
