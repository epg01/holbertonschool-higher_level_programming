#!/usr/bin/python3
"""
    Script to conect to a sql db using MySQLdb client in python
"""

import sys
import MySQLdb

DB_HOST='localhost'
DB_PORT=3306
DB_USER=sys.argv[1]
DB_PASS=sys.argv[2]
DB_NAME=sys.argv[3]

if __name__=='__main__':

        # Conectamos a la base de datos.

        conn = MySQLdb.connect(host=DB_HOST,
                               port=DB_PORT,
                               user=DB_USER,
                               passwd=DB_PASS,
                               db=DB_NAME)

        # Crear un cursor.

        cursor=conn.cursor()

        # Ejecutamos una consulta.

        cursor.execute("""SELECT * FROM states WHERE (name LIKE BINARY 'N%')\
        ORDER BY id ASC""")

        for rows in cursor.fetchall():
            print(rows)

        conn.close()
        cursor.close()
