# TODO: the following 5 functions for CRUD(create, read,update,delete) operations that work with sqlite database called chinook.db

# def create_connection(dbpath):
#   # can add verbose parameter that prints sqlite version used
#   return conn
# def create_artist(conn, artist_name):
#   # do not have to return anything but can use try: inside this function
# def read_artists(conn):  # can add some extra parameters to limit
#   return artists  # can return a list of tuples, or you can create a list of artist objects if you want
# def update_artist(id, new_name):
# def delete_artist(id=None, name=""):
#    # provide deletion by id AND/OR name
# test it by adding you name to artists table smile

import sqlite3


def create_connection(dbpath):
    return sqlite3.connect(dbpath)


con = create_connection('chinook.db')


def create_artist(conn, artist_name):
    cur = conn.cursor()
    cur.execute('INSERT INTO artists (Name) VALUES (?)', (artist_name,))


create_artist(con, "The Beatles")  # we will keep creating new Beatles


def read_artists(conn, limit=10):
    cur = conn.cursor()
    cur.execute('select * from artists limit ?', (limit,))
    return cur.fetchall()


artists = read_artists(con)
print(artists)


def update_artist(id, new_name):
    cur = con.cursor()
    cur.execute('UPDATE artists SET Name = ? WHERE ArtistId = ?',
                (id, new_name))


update_artist(1, "Queens")

artists = read_artists(con, 1000)
print(artists)


def delete_artist(id=None, name=""):
    cur = con.cursor()
    cur.execute('DELETE FROM artists WHERE Name = ? OR ArtistId = ?',
                (name, id))


delete_artist(name="AC/DC")

artists = read_artists(con)
print(artists)

# without commit this will not be saved
con.close()
