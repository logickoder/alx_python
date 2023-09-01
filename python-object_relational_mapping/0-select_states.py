import sys
import MySQLdb


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection_params = {
        "host": "localhost",
        "user": username,
        "passwd": password,
        "db": database,
        "port": 3306,
    }

    try:
        db = MySQLdb.connect(**connection_params)
        cur = db.cursor()

        cur.execute("SELECT * FROM states ORDER BY states.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    main()
