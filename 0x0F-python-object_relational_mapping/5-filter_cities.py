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

    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities "
                   "INNER JOIN states "
                   "ON states.id=cities.state_id "
                   "WHERE states.name= %s "
                   "ORDER BY cities.id ",
                   (MATCH,))

    Datos_input = list()
    for row in cursor.fetchall():
        Datos_input.append(row[1])

    Datos_input = ', '.join(Datos_input)
    print(Datos_input)
    cursor.close()
    conn.close()
