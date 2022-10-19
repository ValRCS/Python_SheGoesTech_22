import sqlite3  # built in module

# https://docs.python.org/3/library/sqlite3.html

con = sqlite3.connect('chinook.db')  # absolute or relative path to database
# for oher SQL databases you might need user/password and possibly port
# Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands:
cur = con.cursor()
row_it = cur.execute('SELECT * FROM albums LIMIT 10')  # returns a row iterator
results_list = [row for row in row_it]  # just list(row_it) would work here as well
print(results_list)

track_it = cur.execute("""SELECT t.Name, 
t.Composer, a.Title, 
a2.Name, g2.Name, mt.Name, t.UnitPrice 
FROM tracks t
JOIN albums a 
ON t.AlbumId = a.AlbumId 
JOIN artists a2 
ON a.ArtistId = a2.ArtistId 
JOIN genres g2 
ON t.GenreId = g2.GenreId 
JOIN media_types mt 
ON t.MediaTypeId = mt.MediaTypeId 
ORDER BY t.Name 
LIMIT 20
OFFSET 60;""")
track_results = [row for row in track_it]  # list(track_it) would work here as well
print(*track_results, sep='\n')  # we unpack the list into individual variables


#
#
def get_album_by_id(cur, id):
    cur.execute('SELECT * FROM albums WHERE AlbumId = ?', (id,))
    return cur.fetchone()


print(get_album_by_id(cur, 16)) # cur - cursor, id - album id
#
#
def insert_album(cur, album: tuple):
    cur.execute('INSERT INTO albums (Title, ArtistId) VALUES (?, ?)',
                album)  # parameters must be in the same order as in the SQL statement


# insert_album(cur, ('The Dark Side of the Moon', 42))  # 42 is probably not Pink Floyd
# insert_album(cur, ('The Dark Side of the Moon', "Bad value"))  # 42 is probably not Pink Floyd
def update_album_title(cur, album: tuple):  # so tuple should have Title first and AlbumId second
    cur.execute('UPDATE albums SET Title = ? WHERE AlbumId = ?',
                album)  # parameters must be in the same order as in the SQL statement
#
#
# # new_albums = get_album_by_name(cur, "Valdis greatest hits 2")
# # print(new_albums)
# insert_album(cur, ("Valdis greatest hits 2", 277))  # album id is auto-incremented, 277 is artist id
#
#
def get_album_by_name(cur, name):
    cur.execute('SELECT * FROM albums WHERE Title LIKE ?', (name,))
    # return cur.fetchone()
    return cur.fetchall()

#
# For Delete practice with Select first
def delete_album_by_id(cur, id):  # so no need to pass in a tuple
    cur.execute('DELETE FROM albums WHERE AlbumId = ?', (id,))
#
#
update_album_title(cur, ("Valdis greatest hits 4 now!", 349))
delete_album_by_id(cur, 350)
#
new_albums = get_album_by_name(cur, "%Best%")
print(*new_albums, sep='\n')
#
# some_album = get_album_by_id(cur, 1)
# print(some_album)
con.commit()  # this should save the database transactions
con.close()

# for more serious SQL work you can use library such as SQLAlchemy
# https://www.sqlalchemy.org/
# SQL library makes it easier to work with databases