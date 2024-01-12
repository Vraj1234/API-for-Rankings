import sqlite3
import random
import string


def populate_users_table():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    for i in range(1, 100001):
        c.execute("INSERT INTO Users (Id, username, karma_score, image_id) VALUES (?, ?, ?, ?)", (i, "randomuser"+str(i), random.randint(0, 7000), i))
    conn.commit()
    conn.close()
    print("Success")

populate_users_table()