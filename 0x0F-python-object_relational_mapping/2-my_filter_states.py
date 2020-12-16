#!/usr/bin/python3
"""
   Script that takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
    MATCH = sys.argv[4]
    CHARSET = 'utf8'

    # Nos conectamos a la base de datos.

    conn = MySQLdb.connect(host=DB_HOST,
                           port=DB_PORT,
                           user=DB_USER,
                           passwd=DB_PASS,
                           db=DB_NAME,
                           charset=CHARSET)

    # Colocamos el cursor.

    cursor = conn.cursor()

    # Ejecutamos el comando

    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' "
                   "ORDER BY states.id ASC ".format(MATCH))

    for row in cursor.fetchall():
        if row[1] == MATCH:
            print(row)

    cursor.close()
    conn.close()
