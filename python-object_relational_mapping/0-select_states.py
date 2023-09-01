#!/usr/bin/python3
# This module lists all states in the database
# imports module MySQLdb
import MySQLdb
import sys


def main():
    database_name = sys.argv[3]
    username = sys.argv[1]
    password = sys.argv[2]

    # Connecting to database in the localhost
    database = MySQLdb.connect(host='localhost', user=username,
                               passwd=password, db=database_name,
                               port=3306)

    # create a cursor
    cur = database.cursor()

    # finding all the states in the database
    cur.execute("SELECT * FROM states ORDER BY states.id")

    # obtaining the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # close cursor
    cur.close()

    # close database
    database.close()


if __name__ == "__main__":
    main()
