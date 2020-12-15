#!/usr/bin/python3
import sys
import MySQLdb

"""
   Script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":

    usrn = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]
    hos_t = "localhost"

    db = MySQLdb.connect(host=hos_t, user=usrn,  passwd=passw, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
