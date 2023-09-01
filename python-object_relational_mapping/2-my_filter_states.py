#!/usr/bin/python3
# This script filters all states where name matches argument
# imports module MySQLdb
import MySQLdb
import sys


def main():
    database_name = sys.argv[3]
    username = sys.argv[1]
    password = sys.argv[2]
    name_searched = sys.argv[4]

    # Connecting to database in the localhost
    database = MySQLdb.connect(host='localhost', user=username,
                               passwd=password, db=database_name,
                               port=3306)

    # create a cursor
    cur = database.cursor()

    # finding all the states in the database beginning with N
    cur.execute("SELECT * FROM states "
                "WHERE name = '{}' AND "
                "name LIKE 'N%' AND "
                "BINARY name NOT LIKE 'n%'"
                "ORDER BY id ASC".format(name_searched))

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
