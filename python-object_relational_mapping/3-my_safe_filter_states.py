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

    # using a parameterized query
    query = ("SELECT * FROM states "
             "WHERE name = %s"
             "ORDER BY id ASC")

    # Execute the query with name searched as parameter
    cur.execute(query, (name_searched,))

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
