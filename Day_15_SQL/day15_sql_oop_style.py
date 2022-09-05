# Martins Klavins
# day-15

import sqlite3


class CRUD:
    """
    created class, so I can skip connection parameter adding to every function, or create it global
    """

    def __init__(self, dbpath):
        self.conn = sqlite3.connect(dbpath)
        self.cur = self.conn.cursor()

    def create_artist(self, artist_name):
        """
        https://docs.python.org/3/library/sqlite3.html
        An SQL statement may use one of two kinds of placeholders: question marks or named placeholders.
        """
        self.cur.execute('INSERT INTO artists (Name) VALUES (?);', (artist_name,))

    def read_artists(self, count, order="ASC"):
        for row in self.cur.execute(f'SELECT * FROM artists ORDER BY Artistid {order} LIMIT {count};'):
            print(row)

    def update_artist(self, id_, new_name):
        self.cur.execute('UPDATE artists SET Name = (?) WHERE Artistid = (?);', (new_name, id_))

    def delete_artist(self, id_=None, name=""):
        self.cur.execute('DELETE FROM artists WHERE Artistid = (?) AND Name = (?);', (id_, name))

    def find_artist(self, by_name=""):
        list_of_results = self.cur.execute('SELECT Artistid FROM artists WHERE Name = (?);', (by_name,)).fetchall()
        return list_of_results[-1][0]  # return last one, unpack tuple's first element

    def save_and_close(self):
        # keep in mind - there will be mess with id incrementation, when this will be executed
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    example = CRUD("chinook.db")
    example.create_artist("default")
    example.read_artists(3, "DESC")
    ID = example.find_artist("default")
    print(ID)
    example.update_artist(ID, "Mārtiņš")
    example.read_artists(3, "DESC")
    example.delete_artist(ID, "Mārtiņš")
    example.read_artists(3, "DESC")
    # example.save_and_close()
