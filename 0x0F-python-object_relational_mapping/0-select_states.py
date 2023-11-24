#!/usr/bin/python3
"""
This module uses MySQLdb module to lists
all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute(
        "SELECT states.id, states.name FROM states ORDER BY states.id ASC;")
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()
    db.close()
