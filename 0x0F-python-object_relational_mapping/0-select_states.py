#!/usr/bin/python3
import MySQLdb
import sys
"""script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    d = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            d=sys.argv[3],
            port=3306
            )

    c = d.cursor()
    c.execute("SELECT * FROM states")

    states = c.fetchall()

    for state in states:
        print(state)

        c.close()
        d.close()
