#!/usr/bin/python3
# This module lists all cities in the database
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

    # finding all the cities in the database
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities, states "
             "WHERE state_id = states.id "
             "ORDER BY cities.id ASC")
    # executing the query
    cur.execute(query)

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
