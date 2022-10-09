#!/usr/bin/python3
"""
List all the states in the db hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', db=argv[3], user=argv[1], passwd='', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
