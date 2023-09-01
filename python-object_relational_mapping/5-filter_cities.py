#!/usr/bin/python3
# This script filters all cities where name matches state
# imports module MySQLdb
import MySQLdb
import sys


def main():
    database_name = sys.argv[3]
    username = sys.argv[1]
    password = sys.argv[2]
    state_name = sys.argv[4]

    # Connecting to database in the localhost
    database = MySQLdb.connect(host='localhost', user=username,
                               passwd=password, db=database_name,
                               port=3306)

    # create a cursor
    cur = database.cursor()

    # using a parameterized query
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE %s = states.name "
             "ORDER BY cities.id ASC")

    # Execute the query with name searched as parameter
    cur.execute(query, (state_name,))

    # obtaining the results
    results = cur.fetchall()

    # Extract city names and join them with commas
    city_names = ", ".join(row[0] for row in results)

    # Display the comma-separated city names
    print(city_names)
    # close cursor
    cur.close()

    # close database
    database.close()


if __name__ == "__main__":
    main()
