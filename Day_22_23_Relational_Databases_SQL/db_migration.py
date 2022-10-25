import sqlite3


def create_tables(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )
    """)


def insert_data(cur):
    cur.execute("""
        INSERT INTO users (username, password) VALUES (?, ?)
    """, ('admin', 'admin'))  # do not save passwords in plain text in database! use salt +  hash function


if __name__ == '__main__':
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    create_tables(cur)
    insert_data(cur)
    conn.commit()
    conn.close()
