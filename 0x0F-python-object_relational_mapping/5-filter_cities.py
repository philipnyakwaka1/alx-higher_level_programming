#!/usr/bin/python3
"""This module lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    input_value = sys.argv[4]
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id\
            = states.id WHERE states.name LIKE %s\
            ORDER BY cities.id ASC;", ('%' + input_value + '%', ))
    results = cursor.fetchall()

    if not results:
        print()
    else:
        city_names = [result[0] for result in results]
        print(', '.join(city_names))

    cursor.close()
    db.close()
