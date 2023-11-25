#!/usr/bin/python3
"""This module lists all states with
a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute(
        f'SELECT * FROM states WHERE states.name\
          LIKE BINARY "{sys.argv[4]}" ORDER BY states.id ASC;')
    results = cursor.fetchall()
    for i in results:
        print(i)
    cursor.close()
    db.close()
