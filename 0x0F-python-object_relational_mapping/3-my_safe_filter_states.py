#!/usr/bin/python3
"""
   Script that takes in arguments and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument. But this time,
   write one that is safe from MySQL injections!
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    MATCH = sys.argv[4]
    # Conectamos la base de datos.
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset='utf8')

    # Colocamos el cursor.

    cursor = conn.cursor()

    # Ejecutamos el cursor.

    cursor.execute("""
    SELECT
        *
    FROM
        states
    WHERE
    name = %(MATCH)s
    """, {
        'MATCH': MATCH
    })

    for row in cursor.fetchall():
        if row[1] == MATCH:
            print(row)

    cursor.close()
    conn.close()
