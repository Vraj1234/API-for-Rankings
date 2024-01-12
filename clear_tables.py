import sqlite3
import random
import string

def populate_images_table():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute("DELETE FROM USERS;")
    c.execute("DELETE FROM IMAGES;")
    
    conn.commit()
    conn.close()
    print("Success")

populate_images_table()