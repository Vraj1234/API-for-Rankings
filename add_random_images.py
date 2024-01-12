import sqlite3
import random
import string

def populate_images_table():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    for i in range(1, 100001):
        random_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        
        url = "https://" + random_url + "_" + str(i)

        c.execute("INSERT INTO Images (Id, url) VALUES (?, ?)", (i, url))

    conn.commit()
    conn.close()
    print("success")

populate_images_table()