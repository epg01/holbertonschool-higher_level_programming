#!/usr/bin/python3
"""
   Script that lists all cities from the database hbtn_0e_4_usa
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]
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

    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states\
    ON states.id = cities.state_id ORDER BY cities.id ASC""")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()
