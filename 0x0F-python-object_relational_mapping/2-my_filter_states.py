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
        "SELECT * FROM states WHERE states.name\
          LIKE BINARY '%{}%' ORDER BY states.id ASC;".format(sys.argv[4]))
    print(f'argv[4]: {sys.argv[4]}')
    print(
        "SELECT * FROM states WHERE states.name LIKE BINARY '%{}%' ORDER BY states.id ASC;".format(sys.argv[4]))
    results = cursor.fetchall()
    for i in results:
        print(i)
    cursor.close()
    db.close()
