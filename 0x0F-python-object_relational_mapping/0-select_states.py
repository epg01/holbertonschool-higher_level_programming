#!/usr/bin/python3
"""
   Script that lists all states from the database hbtn_0e_0_usa
"""


if __name__=='__main__':
    import sys
    import MySQLdb

    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    CHARSET = 'utf8'

    # Nos conectamos a la base de datos

    conn = MySQLdb.connect(host=DB_HOST,
                           port=DB_PORT,
                           user=DB_USER,
                           db=DB_NAME,
                           charset=CHARSET)

    # Colocamos el cursor

    cursor = conn.cursor()

    # Ejecutamos el comando SQL

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in cur.fetchall():
        print(row)

    cursor.close()
    conn.close()
