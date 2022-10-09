#!/usr/bin/python3
"""
 lists all states with a name starting with N (upper N)
 from the db hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(db=argv[3], user=argv[1], passwd=argv[2])
    #conn = MySQLdb.connect(host='localhost', db=argv[3], user=argv[1], passwd='', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
